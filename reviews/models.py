from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from nlprocess.functions import analize_text

import ast

### This set ListField, a custom field, to be instropected by south.
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^arguiew\.reviews\.models\.ListField"])


### Model ListField
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

### Model Product
class Product(models.Model):
	#represent client products
	name = models.CharField('name',max_length=100)
	description = models.CharField('descripton',max_length=200)
	
	def __unicode__(self):
		return self.name

### Model Review
class Review(models.Model):
	#represent users reviews about products
	positive_text = models.CharField('pos',max_length=200)
	negative_text = models.CharField('neg',max_length=200)
	positive_feats = ListField(blank=True, null=True,editable=False)
	negative_feats = ListField(blank=True, null=True,editable=False)
	undecided_feats = ListField(blank=True, null=True,editable=False)
	rating = models.IntegerField(blank=True, null=True)
	product = models.ForeignKey(Product)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.product.name + ' - ' + self.user.username

	def save(self, *args, **kwargs):
		#This is a patch. This should call the propper API to process the text
		#and get the features back. 
		
		self.positive_feats = analize_text(self.positive_text)
		self.negative_feats = analize_text(self.negative_text)

		super(Review,self).save()
		#call to the api that process positive, negative and store it in the dbase. 

### Model ReviewForm
class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ('positive_text','negative_text','rating','product')

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(ReviewForm, self).__init__(*args, **kwargs)
	
	#save is overriden to take into account the user logged in (user passed in the constructor)
	def save(self, *args, **kwargs):
		kwargs['commit']=False #with commit false, first create the object then call object.save
		obj = super(ReviewForm, self).save(*args, **kwargs)
		if self.user:
		   obj.user = self.user
		obj.save()	
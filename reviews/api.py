from tastypie.resources import ModelResource
from reviews.models import Review

class ReviewResource(ModelResource):
    class Meta:
        queryset = Review.objects.all()
        resource_name = 'review'
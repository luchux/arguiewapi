import os

from django import template
from technology.models import Tech

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.tag
def get_documentary(tech_id):
	tech = Tech.objects.get(pk=tech_id)
	docs = [i for i in range(1,5) if tech.__getattribute__('document_'+i)]
	return docs

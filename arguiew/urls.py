from django.conf.urls import patterns, include, url
from django.contrib import admin
from reviews.api import ReviewResource
from nlprocess.views import json_get_features
from reviews.views import index,add
admin.autodiscover()

review_resource = ReviewResource()

urlpatterns = patterns('',

	url(r'^$', index),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(review_resource.urls)),
    url(r'^api/nlprocess/(?P<text>.+)/$', json_get_features),
    url(r'^reviews/add/', add),
)

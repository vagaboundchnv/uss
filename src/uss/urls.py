from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from uss.api.url_api import UrlResource
from uss.api.tags import TagResource
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UrlResource())
v1_api.register(TagResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'uss.views.index', name='index'),
    url(r'^partials/(?P<template_name>[-\w]+.html)$', 'uss.views.partials', name='partials'),
    url(r'^admin/', include(admin.site.urls)),
    (r'api/', include(v1_api.urls)),
    (r'^accounts/', include('registration.urls')),
)

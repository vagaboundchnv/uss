from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'uss.views.index', name='index'),
    url(r'^partials/(?P<template_name>[-\w]+)$', 'uss.views.partials', name='partials'),
    url(r'^admin/', include(admin.site.urls)),
)

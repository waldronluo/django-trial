from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from privatesite.views import index, staticFileAccess

urlpatterns = [
        url(r'^$', index),
        #url(r'^statics/.*', views.serve, {'document_root', settings.STATIC_URL}),
        url(r'^statics/.*', views.serve, {'document_root':'~/Code/django/test/myblog/privatesite/statics/css', 'show_indexes': True}),
        ]


# coding: utf-8

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "django.views.debug.default_urlconf"),   # 初期画面も出したい
    url(r'^polls/', include("polls.urls")),
    url(r'^admin/', include(admin.site.urls)),
)

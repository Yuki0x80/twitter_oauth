# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
     #url(r'^$', 'twitter_oauth.views.home', name='home'),
     #url(r'^twitter_oauth/', include('twitter_oauth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Top Page
    url(r'^oauth/$', 'oauth.views.index', name='index'),
    # Twitter OAuth Authenticate
    url(r'^oauth/get/$', 'oauth.views.get', name='get'),
    # Callback
    url(r'^oauth/get_callback/$', 'oauth.views.get_callback', name='get_callback'),
    # Redirect Page of after Authenticate
    url(r'^oauth/oauth_index/$', 'oauth.views.oauth_index', name='oauth_index'),
    # Tweet
    url(r'^oauth/post/$', 'oauth.views.post', name='post'),
]

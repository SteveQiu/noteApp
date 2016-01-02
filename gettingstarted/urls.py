from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import note.views
import hello.views

urlpatterns = patterns('',
    url(r'^profile/', include('note.urls'),name='profile'),
    url(r'^db/?', hello.views.db, name='db'),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'/?', note.views.index, name='index'),
)

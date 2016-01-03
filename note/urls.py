from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^signout/?$', views.signout, name='signout'),
    url(r'^dashboard/?$', views.dashboard, name='dashboard'),
    url(r'^create/?$', views.create, name='create'),
    url(r'^$', views.redirect, name='index'),
]

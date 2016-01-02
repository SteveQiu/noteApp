from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/?', views.signup, name='signup'),
    url(r'^signin/?', views.signin, name='signin'),
    url(r'^(?P<account_id>[0-9]+)/?$', views.dashboard, name='dashboard'),
    url(r'^$', views.redirect, name='index'),
]

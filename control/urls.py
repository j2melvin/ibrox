from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^live_feed$', views.live_feed, name='live_feed'),
]

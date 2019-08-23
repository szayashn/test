from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout/(?P<id>\d+)$', views.checkout),
    url(r'^process$', views.process)
]
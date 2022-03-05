from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^dogs/$', views.dog_list),
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', views.dog_detail),
]
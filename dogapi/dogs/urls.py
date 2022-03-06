from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^dogs/$', views.DogList.as_view(), name='dog_list'),
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', views.DogDetail.as_view(), name='dog_detail'),
    re_path(r'^breeds/$', views.BreedList.as_view(), name='breed_list'),
    re_path(r'^breeds/(?P<pk>[0-9]+)/$', views.BreedDetail.as_view(), name='breed_detail'),
    re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
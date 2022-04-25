from django.urls import path, include
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.data_view, name='data'),
    path('data/',  views.data_view, name='data'),
]

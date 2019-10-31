from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='defaultIndex'),
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
]

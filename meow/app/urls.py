from django.urls import path

from meow.app import views

urlpatterns = [
    path('', views.index, name='index'),
]

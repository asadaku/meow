from django.urls import path

from meow.app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_a_cat/', views.get_a_cat, name='get_a_cat'),
]
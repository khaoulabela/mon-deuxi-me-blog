from django.urls import path
from . import views

urlpatterns = [
    path('', views.listes_list, name='listes_list'),

]
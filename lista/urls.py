from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_list, name='ingredient_list'),
    path('ingredient/new/', views.ingredient_new, name='ingredient_new'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_list, name='ingredient_list'),
    path('ingredient/new/', views.ingredient_new, name='ingredient_new'),
    path('ingredient/<int:pk>/check/', views.ingredient_check, name='ingredient_check'),
    path('ingredient/<int:pk>/edit/', views.ingredient_edit, name='ingredient_edit'),
]
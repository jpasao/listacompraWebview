from django.urls import path
from ..views import ingredient_views

ingredient_urlpatterns = [
    path('', ingredient_views.ingredient_list, name='home'),
    path('ingredients/', ingredient_views.ingredient_list, name='ingredient_list'),
    path('ingredient/new/', ingredient_views.ingredient_new, name='ingredient_new'),
    path('ingredient/<int:pk>/check/', ingredient_views.ingredient_check, name='ingredient_check'),
    path('ingredient/<int:pk>/edit/', ingredient_views.ingredient_edit, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete/', ingredient_views.ingredient_delete, name='ingredient_delete'),
    path('ingredient/<int:pk>/increase/', ingredient_views.ingredient_increase, name='ingredient_increase'),
    path('ingredient/<int:pk>/decrease/', ingredient_views.ingredient_decrease, name='ingredient_decrease'),
]
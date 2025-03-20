from django.urls import path
from ..views import meal_views

meal_urlpatterns = [
    path('meals/', meal_views.meal_list, name='meal_list'),
    path('meal/new/', meal_views.meal_new, name='meal_new'),
    path('meal/<int:pk>/edit/', meal_views.meal_edit, name='meal_edit'),
    path('meal/<int:pk>/choose/', meal_views.meal_choose, name='meal_choose'),
    path('meal/<int:pk>/choose_dinner/', meal_views.meal_choose_dinner, name='meal_choose_dinner'),
    path('meal/<int:pk>/check/', meal_views.meal_check, name='meal_check'),
    path('meal/<int:pk>/delete/', meal_views.meal_delete, name='meal_delete'),
    path('meal/<int:pk>/ingredients/', meal_views.meal_get_ingredients, name='meal_get_ingredients'),
    path('meal/<int:pk>/ingredients/save/', meal_views.meal_set_ingredients, name='meal_set_ingredients'),
]
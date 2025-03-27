from django.urls import path

from ..views import other_views

otherchild_urlpatterns = [
    path('others/', other_views.other_list, name='other_list'),
    path('other/new/', other_views.other_new, name='other_new'),
    path('other/<int:pk>/edit/', other_views.other_edit, name='other_edit'),
    path('other/<int:pk>/check/', other_views.other_check, name='other_check'),
    path('other/<int:pk>/uncheck/', other_views.other_uncheck, name='other_uncheck'),
    path('other/<int:pk>/delete/', other_views.other_delete, name='other_delete'),
]

otherparent_urls = [
    path('others/parent/', other_views.other_parent_list, name='other_parent_list'),
    path('other/parent/new/', other_views.other_parent_new, name='other_parent_new'),
    path('other/parent/<int:pk>/edit/', other_views.other_parent_edit, name='other_parent_edit'),
    path('other/parent/<int:pk>/delete/', other_views.other_parent_delete, name='other_parent_delete'),
]

other_urlpatterns = otherchild_urlpatterns + otherparent_urls
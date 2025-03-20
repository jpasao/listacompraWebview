from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from django.views.static import serve

from webview import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('lista.urls')),
]
urlpatterns += [re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, })]
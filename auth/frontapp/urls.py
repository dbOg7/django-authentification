# django_project/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerView, name="register"),
    path('', views.HomeViews.as_view(template_name='home.html'), name="home.html"),
]

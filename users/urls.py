from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('', views.ProfilePage.as_view(), name='profile_page'),
    path('edit/', views.ProfileUpdateView.as_view(), name='profile_update')
]
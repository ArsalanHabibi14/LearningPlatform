from django.urls import path
from . import views


urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('contact/', views.ContactCreateView.as_view(), name='contact_create_view'),
]
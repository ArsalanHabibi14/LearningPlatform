from django.urls import path
from . import views

urlpatterns = [
	path('profile/', views.ProfilePage.as_view(), name='profile_list_view'),
	path('profile/edit/', views.ProfileEditPage.as_view(), name='profile_update_view'),
	path('courses/', views.CourseListView.as_view(), name='course_list_view'),
	path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_list_view'),
]
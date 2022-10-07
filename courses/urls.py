from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoursesPage.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('categories/', views.categories_page, name='categories'),
]
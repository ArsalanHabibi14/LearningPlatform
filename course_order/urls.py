from django.urls import path
from . import views

urlpatterns = [
    path("add_user/<int:course_id>/", views.add_user_order, name='add_order'),
    path("remove/<int:course_id>/", views.remove_user_order, name='remove_order')
]
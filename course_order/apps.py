from django.apps import AppConfig


class CourseOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_order'

    def ready(self):
        from . import signals

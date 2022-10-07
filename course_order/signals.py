from django.db.models.signals import pre_save, post_save, post_delete
from .models import Order, OrderDetail
from courses.models import Course


def add_student(sender, created, instance, **kwargs):
    if created:
        get_course = Course.objects.get(id=instance.course.id)
        get_course.student += 1
        get_course.save()


post_save.connect(add_student, OrderDetail)


def delete_student(sender, instance, **kwargs):
    get_course = Course.objects.get(id=instance.course.id)
    get_course.student -= 1
    get_course.save()


post_delete.connect(delete_student, OrderDetail)

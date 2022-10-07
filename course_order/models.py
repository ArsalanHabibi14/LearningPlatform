from django.db import models
from users.models import Profiles
from courses.models import Course
from django.forms import ValidationError


class Order(models.Model):
    user = models.ForeignKey(Profiles, on_delete=models.CASCADE, unique=True)
    is_pay = models.BooleanField(default=False, verbose_name="Is Pay / Is not Pay")
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='')

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.user.user_type == "teach":
            raise ValidationError("The User Should be a Student!")


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title

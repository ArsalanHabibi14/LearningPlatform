import os
from django.db import models
from django.forms import ValidationError
from users.models import Profiles
from .utils import file_upload


class Category(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.title


class Course(models.Model):
    teacher = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="courses/")
    student = models.IntegerField(null=True, blank=True, default=0)
    tag = models.ManyToManyField("Tag")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def clean(self):
        if self.teacher.user_type == "stu":
            raise ValidationError("The Teacher type should be the teacher")


class Videos(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def get_extension(self):
        basename = os.path.basename(str(self.video))
        name, ext = os.path.splitext(str(basename))
        return ext

    def clean(self):
        if self.get_extension().lower() != ".mp4":
            raise ValidationError("Your File Should be a video with the mp4 format!")
        return super().clean()


class Tag(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="tags/", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ----- {self.body[:30]}'

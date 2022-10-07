import uuid
from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="skills/", null=True, blank=True)
    def __str__(self):
        return self.title

class Profiles(models.Model):
    USER_TYPE = (
        ('teach', "Teacher"),
        ('stu', "Student"),
        ('both', "Both"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200, choices=USER_TYPE)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='users/', default="avatar.svg", null=True, blank=True)
    skills = models.ManyToManyField(Skill,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    website_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    linkdin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    short_intro = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
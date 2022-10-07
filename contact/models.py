from django.db import models
from users.models import Profiles

class Contact(models.Model):
	username = models.CharField(max_length=200)
	last_name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=150, null=True, blank=True)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username

class Services(models.Model):
	title = models.CharField(max_length=120)
	about_service = models.TextField()

	def __str__(self):
		return self.title

class About(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	address = models.CharField(max_length=2000, null=True, blank=True)
	phone = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	about_us = models.TextField(null=True, blank=True)
	copy_right = models.CharField(max_length=200, null=True, blank=True)
	logo_image = models.ImageField(upload_to='site_log/', null=True, blank=True)

class Instructor(models.Model):
	user = models.ForeignKey(Profiles, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + self.user.last_name
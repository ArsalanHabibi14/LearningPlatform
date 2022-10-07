from django.db.models.signals import pre_save, post_save
from .models import Course, Videos
from django.core.mail import send_mail
from users.models import Profiles
import os

def check_teacher(sender, instance, **kwargs):
    teacher_type = instance.teacher.user_type
    print(teacher_type)
pre_save.connect(check_teacher, Course)


def created_course(sender, created, instance, **kwargs):
	if created:
		course = instance
		profiles = Profiles.objects.all()
		for profile in profiles:
			send_mail("New Course", f'{course.title} \n {course.image}', 'ibrahimarsalan94@gmail.com', [profile.email])

post_save.connect(created_course, Course)


def file_title(sender, instance, *args, **kwargs):
	if not instance.title:
		basename = os.path.basename(instance.video.path)
		name, ext = os.path.splitext(basename)
		instance.title = name

pre_save.connect(file_title, sender=Videos)
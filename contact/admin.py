from django.contrib import admin
from .models import Contact, Instructor, Services, About

admin.site.register(Contact)
admin.site.register(Instructor)
admin.site.register(Services)
admin.site.register(About)
from django.contrib import admin
from .models import Course, Tag, Category, Videos, Comment
from course_order.models import OrderDetail
from django import forms

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['image'].widget.template_name = "courses/image.html"

class OrderDetailStackInline(admin.StackedInline):
    model = OrderDetail


class CourseAdmin(admin.ModelAdmin):
	form = CourseForm
    # list_display = ['__str__', 'student', 'price']
    # list_editable = ['price', 'student']
    # inlines = [
    #     OrderDetailStackInline
    # ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Videos)
admin.site.register(Comment)
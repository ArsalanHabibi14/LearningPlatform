from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({'class' : "form-control"})
		self.fields['message'].widget.attrs.update({"style" : "height : 150px"})
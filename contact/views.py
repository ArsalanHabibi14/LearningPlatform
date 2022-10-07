from django.views.generic import ListView, CreateView, DetailView
from .models import Contact, Instructor, About, Services
from .forms import ContactForm
from courses.models import Course
from django.shortcuts import render


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = '/'

def home_page(request):
    all_courses = Course.objects.all().order_by('-student')[:6]
    instructors = Instructor.objects.all()[:5]
    services = Services.objects.all()
    about_us = About.objects.first()
    context = {
        'courses': all_courses,
        'instructors' : instructors,
        'about' : about_us,
        'services' : services
    }
    return render(request, 'index.html', context)

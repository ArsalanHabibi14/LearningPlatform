from django.shortcuts import render
from courses.models import Course
from users.models import Profiles




def header(request):
    context = {}
    if request.user.is_authenticated:
        profile = Profiles.objects.get(user=request.user)
        context['profile'] = profile

    return render(request, 'shared/header.html', context)


def error_page(request, exception):
    context = {}
    return render(request, '404.html', context)

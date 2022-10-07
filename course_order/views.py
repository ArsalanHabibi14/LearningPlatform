from courses.models import Course
from .models import Order, OrderDetail
from users.models import Profiles
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def add_user_order(request, course_id):
    get_course = Course.objects.get(id=course_id)
    get_profile = Profiles.objects.get(user=request.user)
    user_order = Order.objects.filter(user=get_profile)
    if user_order.exists():
        get_order_deatil = OrderDetail.objects.filter(order=user_order.first(), course=get_course)
        if not get_order_deatil.exists() and get_course.teacher != get_profile:
            instance = OrderDetail.objects.create(order=user_order.first(), course=get_course)
            return redirect(f'/courses/{course_id}/')

        else:
            messages.error(request, 'You can\'t enroll for this course!')
            return redirect(f'/courses/{course_id}/')
    else:
        created_order = Order.objects.create(user=get_profile)
        OrderDetail.objects.create(order=created_order, course=get_course)
        return redirect(f'/courses/{course_id}/')

@login_required(login_url='/login/')
def remove_user_order(request, course_id):
    get_course = Course.objects.get(id=course_id)
    get_profile = Profiles.objects.get(user=request.user)
    user_order = Order.objects.filter(user=get_profile)
    if user_order.exists():
        get_order_deatil = OrderDetail.objects.get(order=user_order.first(), course=get_course)
        if get_order_deatil is None and get_course.teacher != get_profile:
            return redirect(f'/courses/{course_id}/')

        else:
            get_order_deatil.delete()
            return redirect(f'/courses/{course_id}/')
    else:
        return redirect(f'/courses/{course_id}/')
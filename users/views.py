from .models import Profiles
from django.shortcuts import render, redirect
from .forms import CustomUserForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView
)
from course_order.models import Order, OrderDetail
from django.contrib import messages




def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return message.error(request, 'username or password is wrong!')
    return render(request, 'users/login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CustomUserForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("/")
    return render(request, 'users/register.html', context)


class ProfilePage(DetailView):
    template_name = 'users/profile.html'

    def get_queryset(self):
        user = self.request.user
        profile = Profiles.objects.filter(user=user)
        self.kwargs['pk'] = profile.first().id
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_order = Order.objects.filter(user=self.get_queryset().first())
        get_order_detail = OrderDetail.objects.filter(order=get_order.first())
        context['order_detail'] = get_order_detail
        return context


class ProfileUpdateView(UpdateView):
    template_name = 'users/user_form.html'
    form_class = UserUpdateForm
    success_url = '/profile/'

    def get_queryset(self):
        user = self.request.user
        profile = Profiles.objects.filter(user=user)
        self.kwargs['pk'] = profile.first().id
        return profile

    def form_valid(self, form):
        return super().form_valid(form)

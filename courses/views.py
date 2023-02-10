from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Course, Videos
from django.shortcuts import render, redirect
from course_order.models import Order, OrderDetail
from users.models import Profiles
from .models import Comment
from .forms import CommentForm
from django.db.models import Q
from pymediainfo import MediaInfo
from django.contrib.auth.mixins import LoginRequiredMixin


class CoursesPage(ListView):
    template_name = "courses/list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q is not None:
            courses = Course.objects.filter(
                Q(title__startswith=q)
                | Q(content__icontains=q)
                | Q(tag__title__icontains=q)
            ).distinct()
            return courses
        else:
            return Course.objects.all()


class CourseDetailView(CreateView):
    model = Comment
    template_name = "courses/detail.html"
    form_class = CommentForm
    login_url = reverse_lazy('login_page')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            get_profile = Profiles.objects.filter(user=self.request.user)
            context["profile"] = get_profile
        get_pk = self.kwargs["pk"]
        get_course = Course.objects.get(id=get_pk)
        context["object"] = get_course

        main_course = Course.objects.get(id=self.kwargs["pk"])
        related_courses = main_course.category.all()
        context["related_courses"] = related_courses
        video = Videos.objects.filter(course=main_course).first()
        context["video"] = video
        all_videos = Videos.objects.filter(course=main_course)
        # for s in all_videos:
        #     get_time_video = MediaInfo.parse(s.video.path)
        #     for track in get_time_video.tracks:
        #         print(track.to_data()[3][:])
        # ================ User Order ==================
        get_order = Order.objects.get(user=get_profile.first())
        get_order_detail = OrderDetail.objects.filter(
            order=get_order, course=main_course
        )
        print(get_order_detail.exists())
        context["order_detail"] = get_order_detail
        return context

    def form_valid(self, form):
        get_pk = self.kwargs["pk"]
        get_course = Course.objects.get(id=get_pk)
        get_profile = Profiles.objects.filter(user=self.request.user).first()
        form.instance.user = get_profile
        form.instance.course = get_course
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.kwargs["pk"]})


def categories_page(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories.html", context)

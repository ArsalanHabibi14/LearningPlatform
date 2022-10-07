from rest_framework import generics
from users.models import Profiles
from .serializers import ProfileSerializer, CourseSerializer, ProfileSerializerEdit
from courses.models import Course

class ProfilePage(generics.RetrieveAPIView):
	serializer_class = ProfileSerializer

	def get_queryset(self):
		get_profile = Profiles.objects.filter(user=self.request.user)
		self.kwargs['pk'] = get_profile.first().id
		return get_profile

class ProfileEditPage(generics.RetrieveUpdateAPIView):
	serializer_class = ProfileSerializerEdit

	def get_queryset(self):
		get_profile = Profiles.objects.filter(user=self.request.user)
		self.kwargs['pk'] = get_profile.first().id
		return get_profile

class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
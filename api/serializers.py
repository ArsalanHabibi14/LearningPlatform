from rest_framework import serializers
from users.models import Profiles, Skill
from courses.models import Course

class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = ['title']

class ProfileSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source="user.username")
	skills = SkillSerializer(many=True)
	class Meta:
		model = Profiles
		fields = '__all__'

class ProfileSerializerEdit(serializers.ModelSerializer):
	class Meta:
		model = Profiles
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'
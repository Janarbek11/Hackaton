from rest_framework import serializers
from .models import *
# from django.contrib.auth import


class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


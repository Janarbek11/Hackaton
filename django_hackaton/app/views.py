from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializers
    queryset = Course.objects.all()
    permission_classes = IsAuthenticated

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializers
    queryset = Course.objects.all()
    permission_classes = IsOwnerOrReadOnly


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseDetailSerializers
    queryset = Course.objects.all()

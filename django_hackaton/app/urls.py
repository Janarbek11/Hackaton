from django.urls import path
from .views import *


urlpatterns = [
    path('course/create/', CourseCreateView.as_view()),
    path('course/read/', CourseListView.as_view()),
    path('course/update/<int:pk>', CourseDetailView.as_view()),
]

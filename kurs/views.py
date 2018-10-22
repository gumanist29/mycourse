from .models import Course, Contact, Branch, Category
from kurs.serializers import CourseSerializer, ContactSerializer, BranchSerializer, CategorySerializer
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course
    serializer_class = CourseSerializer

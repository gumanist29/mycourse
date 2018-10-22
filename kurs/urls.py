from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from kurs import views



urlpatterns = [
    path('kurs/', views.CourseList.as_view()),
    path('kurs/<int:pk>/', views.CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
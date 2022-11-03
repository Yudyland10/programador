# apis/urls.py
from django.urls import path
from .views import InstructorAPIView
urlpatterns = [
path("", InstructorAPIView.as_view(), name="instructor_list"),
]
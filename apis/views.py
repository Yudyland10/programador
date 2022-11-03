# apis/views.py
from rest_framework import generics
from programer.models import Instructor
from .serializers import InstructorSerializer

class InstructorAPIView(generics.ListAPIView):
  queryset = Instructor.objects.all()
  serializer_class = InstructorSerializer

class DetailTodo (generics.RetrieveAPIView ):
 queryset = Instructor.objects.all()
 serializer_class = InstructorSerializer
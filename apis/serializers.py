# apis/serializers.py
from rest_framework import serializers
from programer.models import Instructor
class InstructorSerializer (serializers .ModelSerializer ):
 class Meta:
  model = Instructor
  fields = ("id","cc", "name" , "email", "telefono", "areaOrientar", "rol")
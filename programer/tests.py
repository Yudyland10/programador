
  
	# todos/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Instructor
class InstructorModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
   cls.instructor = Instructor.objects.create(
   cc="1117504390",
	 name="Lorena Fierro",
	 email="ylfierro@sena.edu.co",
	 telefono="3213918021",
	 areaOrientar="software-ofimatica",
	 rol="instructor",
     )
  def test_model_content(self):
   self.assertEqual(self.instructor.cc, "1117504390")
   self.assertEqual(self.instructor.name, "Lorena Fierro")
   self.assertEqual(self.instructor.email, "ylfierro@sena.edu.co")
   self.assertEqual(self.instructor.telefono, "3213918021")
   self.assertEqual(self.instructor.areaOrientar, "software-ofimatica")
   self.assertEqual(self.instructor.rol, "instructor")

  def test_api_listview(self):
   response = self.client.get(reverse("instructor_list"))
   self.assertEqual(response.status_code, status.HTTP_200_OK)
   self.assertEqual(Instructor.objects.count(), 1)
   self.assertContains(response, self.instructor)
  def test_api_detailview(self):
   response = self.client.get(
   reverse("instructor_detail", kwargs={"pk": self.instructor.id}),
   format="json"
)
   self.assertEqual(response.status_code, status.HTTP_200_OK)
   self.assertEqual(Instructor.objects.count(), 1)
   self.assertContains(response, "First Instructor")

  
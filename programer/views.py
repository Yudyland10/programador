
from django.views.generic import ListView
from .models import Instructor
class InstructorListView (ListView):
    model = Instructor
    template_name = "instructor_list.html"

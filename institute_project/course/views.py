from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import course_master

# Create your views here.
class NewCourse(CreateView):
    model = course_master
    fields = '__all__'

class ViewCourse(ListView):
    model = course_master
    context_object_name = 'courses'

class UpdateCourse(UpdateView):
    model = course_master
    fields = '__all__'

class DeleteCourse(DeleteView):
    model = course_master
    success_url ='/course/view'






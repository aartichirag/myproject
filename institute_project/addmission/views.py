from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import addmission_details

# Create your views here.
class NewAddmission(CreateView):
    model = addmission_details
    fields = '__all__'
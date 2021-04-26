from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import payment_details

#Create your views here.

class NewPayment(CreateView):
    model = payment_details
    fields = '__all__'

class ViewPayment(ListView):
    model = payment_details
    context_object_name = 'payments'

class UpdatePayment(UpdateView):
    model = payment_details
    fields = '__all__'

class DetailPayment(DetailView):
    model = payment_details
    template_name = 'payment/invoice-print.html'

class DeletePayment(DeleteView):
    model = payment_details
    success_url = '/payment/view'
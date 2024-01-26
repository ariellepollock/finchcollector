from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from . models import Finch

from . forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()

    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', { 
        'finch': finch, 'feeding_form': feeding_form 
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # success_url = '/finches/{finch_id}'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import classofvechiles
from .models import vechiles
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form ={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
def vechile(request):
    dict_vechs = {
        'vechs': vechiles.objects.all()
    }
    return render(request, 'vechiles.html', dict_vechs)
def contact(request):
    return render(request, 'contact.html')
def classofvechile(request):
    dict_clsovhls={
        'clsovhls':classofvechiles.objects.all()
    }
    return render(request, 'classofvechiles.html', dict_clsovhls)

    
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from .models import *
# Create your views here.
import matplotlib.pyplot as plt
import numpy as np

def image_view(request):
   
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
#            images = image_model.objects.all()
            images = image_model.objects.last()
            #return render(request, 'image_upload/last_image.html', {'images': images})
            #return redirect('success')
            return redirect('result')

    else:
        form = imageForm()
    return render(request, 'image_upload/detail.html', {'form': form})
    

def success(request):
    return HttpResponse('Successfully uploaded')


def display_image_all(request):
    if request.method == 'GET':
        images = image_model.objects.all()
        return render(request, 'image_upload/show_images.html', {'images': images})


def display_last(request):
    if request.method == 'GET':
        images = image_model.objects.last()
        return render(request, 'image_upload/last_image.html', {'images': images})

def display_result(request):
    images=image_model.objects.last()

    results='1'
    return render(request,'image_upload/results.html',{'images':images,'results':results})
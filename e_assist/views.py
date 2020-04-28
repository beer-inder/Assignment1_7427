from django.shortcuts import render
from django.http import HttpResponse

def home(request):
#    return HttpResponse('<h1>Home</h1>')
    return render(request, 'e_assist/home.html', {'title': "Home"})

def about(request):
    return render(request, 'e_assist/about.html', {'title': "About"})
#    return render(request, 'e_assist/about.html')

# Create your views here.

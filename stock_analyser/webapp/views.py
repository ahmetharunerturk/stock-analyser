from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'index.html')

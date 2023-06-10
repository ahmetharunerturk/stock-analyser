from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'index.html')

def Features(request):
    return render(request, 'features.html')

def Pricing(request):
    return render(request, 'pricing.html')

def FAQs(request):
    return render(request, 'faqs.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

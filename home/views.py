from django.shortcuts import render


def home(request):
    return render(request, '02_dark-index-2.html')

def contact(request):
    return render(request, 'contact.html')


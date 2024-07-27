from django.shortcuts import render


def home(request):
    return render(request, '02_dark-index-2.html')


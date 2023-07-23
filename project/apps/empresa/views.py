from django.shortcuts import render


def home(request):
    return render(request, "empresa/index.html")
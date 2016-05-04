from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'first_name': 'John',
               'last_name': 'Doe'}
    return render(request, 'control/index.html', context)

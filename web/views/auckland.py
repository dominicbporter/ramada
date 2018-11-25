from django.http import request
from django.shortcuts import render


def auckland_view(request):
    return render(request, 'auckland.html', context={})
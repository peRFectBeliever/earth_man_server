from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def collector(request):
    return render(request, 'collector.html', {})

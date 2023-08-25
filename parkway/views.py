from django.conf import settings
from django.shortcuts import render


def home(request):
    context = {'page_name': 'home'}
    return render(request, 'index.html', context)


def about(request):
    context = {
        'page_name': 'about',
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'about.html', context)


def team(request):
    context = {'page_name': 'team'}
    return render(request, 'team.html', context)


def contact(request):
    context = {'page_name': 'contact'}
    return render(request, 'contact.html', context)
from django.shortcuts import render
from .utils import spotify_helper


def home(request):
    context = spotify_helper(request)
    return render(request, 'return_song/home.html', context)

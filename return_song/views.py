from django.shortcuts import render, redirect
from .forms import SearchForm

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = '054559634ac34a19afa7d28b361b8381'
os.environ['SPOTIPY_CLIENT_SECRET'] = '29c71a1fb755427cad29e6335252130b'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def home(request):
    artist_name, top_track, error, searched = '', '', '', 0
    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.save()
        # response = request.POST
        artist_choice = request.POST['artist_search']

        try:
            result = spotify.search(q=f'artist:{artist_choice}')
            artist_id = result['tracks']['items'][0]['artists'][0]['id']

            artist = spotify.artist(f'{artist_id}')
            results = spotify.artist_top_tracks(f'spotify:artist:{artist_id}')

            searched = 1
            artist_name = artist['name']
            top_track = results['tracks'][0]['name']

        except IndexError:
            searched = 2
            error = 'We can\'t find an artist by that name. Try again!'

        form = SearchForm()
        # return redirect('answer')

    context = {
        'form': form,
        'artist_name': artist_name,
        'top_track': top_track,
        'error': error,
        'searched': searched
    }
    return render(request, 'return_song/home.html', context)


# def answer(request):
#     form = SearchForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'return_song/answer.html', context)


# def search_view(request):
#     form = SearchForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = SearchForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'return_song/search.html', context)

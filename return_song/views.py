from django.shortcuts import render
from .forms import SearchForm

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     scope='user-library-read',
#     client_id='SPOTIPY_CLIENT_ID',
#     client_secret='SPOTIPY_CLIENT_SECRET',
#     redirect_uri='http://127.0.0.1:8000/'
# ))

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
))


def home(request):
    artist_name, top_track, error, searched = '', '', '', 0
    artist_choice = ''
    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.save()
        try:
            artist_choice = request.POST['artist_search']
        except EOFError:
            print(EOFError)

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

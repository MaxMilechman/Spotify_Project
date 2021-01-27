import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

from return_song.forms import SearchForm

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
))


def spotify_helper(request):
    artist_name, top_track, error, searched = '', '', '', 0
    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.save()
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

    context = {
        'form': form,
        'artist_name': artist_name,
        'top_track': top_track,
        'error': error,
        'searched': searched
    }

    return context

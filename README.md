![alt-text](return_song/static/return_song/title_image_rm.png)

Top Track is a web-based Python application where a user can search for any artist, and the top track of that artist will be displayed.

## How to use Top Track

Simply navigate to toptrack2020.herokuapp.com and search for any artist in the search bar. It's that easy!

![alt-text](return_song/static/return_song/toptrackgif.gif)

## How Top Track works

Top Track is a Django (3.1.4) application written in Python (3.9.0). It uses Spotipy (2.16.1) to access Spotify's API and return the most popular song/track for any given artist.

## Installation 

* Download the ZIP of this project
* Naviagte to the projects root directory in your command line
* Type 'pip install -r requirements.txt' to automatically install all the project dependencies
* Type 'python manage.py runserver' to run the server locally
* Click on the hyperlink to open the website or simply navigate to localhost:8000 in your browser to get started!
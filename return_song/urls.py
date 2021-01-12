from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home),
    # path('answer/', views.answer, name='return_song-answer')
    # path('search/', search_view),
]
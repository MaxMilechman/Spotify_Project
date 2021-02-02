from django.db import models


class Search(models.Model):
    artist_search = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.artist_search}'

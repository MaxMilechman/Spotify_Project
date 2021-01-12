from django.db import models


class Search(models.Model):
    artist_search = models.CharField(max_length=100, default='')
# from asyncio.windows_events import INFINITE
from datetime import datetime
from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField(default = 0)
    
    
class Song(models.Model):
    title = models.CharField(max_length = 40)
    rel_date = models.DateField(default = datetime.today)
    likes = models.IntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    
    
class Lyric(models.Model):     
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
# Create your models here.

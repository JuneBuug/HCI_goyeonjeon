from django.db import models

# Create your models here.

class CheerioSong(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()
    song_url = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class CheerioDance(models.Model) :
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class Score(models.Model) :
    year = models.CharField(max_length=20)
    baseball_k = models.CharField(max_length=20)
    baseball_y = models.CharField(max_length=20)
    baseball_r = models.CharField(max_length=20)
    baseketball_k = models.CharField(max_length=20)
    baseketball_y = models.CharField(max_length=20)
    baseketball_r = models.CharField(max_length=20)
    ice_k = models.CharField(max_length=20)
    ice_y = models.CharField(max_length=20)
    ice_r = models.CharField(max_length=20)
    football_k = models.CharField(max_length=20)
    football_y = models.CharField(max_length=20)
    football_r = models.CharField(max_length=20)
    soccer_k = models.CharField(max_length=20)
    soccer_y = models.CharField(max_length=20)
    soccer_r = models.CharField(max_length=20)
    total_k = models.CharField(max_length=20)
    total_tie = models.CharField(max_length=20)
    total_y = models.CharField(max_length=20)
    total_r = models.CharField(max_length=20)

    def __str__(self):
        return self.year
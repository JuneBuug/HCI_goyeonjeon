from django.db import models

# Create your models here.

class CheerioSong(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()
    song_url = models.CharField(max_length=512)

    def __str__(self):
        return self.title
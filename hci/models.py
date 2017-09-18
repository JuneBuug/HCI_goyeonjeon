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

class Match(models.Model) :
    name_kr = models.CharField(max_length=24) # 경기 한글명
    name_en = models.CharField(max_length=64) # 경기 영어명
    score_kr = models.CharField(max_length=24) # 고려대 점수
    score_ys = models.CharField(max_length=24) # 연세대 점수
    updated_titme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_kr


class Restaurant(models.Model) :
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.name
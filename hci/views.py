from django.shortcuts import render
from .models import CheerioSong,Scoring
# Create your views here.

def song_list(request) :
    songs = CheerioSong.objects.all()
    return render(request,'hci/song_list.html',{'songs': songs})


def main(request) :
    scores = Scoring.objects.all()
    return render(request,'hci/main.html',{'scores':scores})
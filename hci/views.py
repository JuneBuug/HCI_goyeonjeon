from django.shortcuts import render
from .models import CheerioSong
# Create your views here.

def song_list(request) :
    songs = CheerioSong.objects.all()
    return render(request,'hci/song_list.html',{'songs': songs})
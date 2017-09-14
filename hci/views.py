from django.shortcuts import render
from .models import CheerioSong,CheerioDance,Score,Match
# Create your views here.

def song_list(request) :
    songs = CheerioSong.objects.all()
    return render(request,'hci/song_list.html',{'songs': songs})

def dance_list(request) :
    dances = CheerioDance.objects.all()
    return render(request,'hci/dance_list.html',{'dances': dances})

def main(request) :
    matches = Match.objects.all().order_by('updated_titme').reverse()
    return render(request,'hci/main.html',{'matches':matches})

def history(request) :
    scores = Score.objects.all()
    return render(request,'hci/history.html',{'scores':scores})
from django.shortcuts import render
from .models import CheerioSong,Scoring,CheerioDance
# Create your views here.

def song_list(request) :
    songs = CheerioSong.objects.all()
    return render(request,'hci/song_list.html',{'songs': songs})

def dance_list(request) :
    dances = CheerioDance.objects.all()
    return render(request,'hci/dance_list.html',{'dances': dances})

def main(request) :
    scores = Scoring.objects.all()
    return render(request,'hci/main.html',{'scores':scores})


def history(request) :
    scores = Scoring.objects.all()
    return render(request,'hci/history.html',{'scores':scores})
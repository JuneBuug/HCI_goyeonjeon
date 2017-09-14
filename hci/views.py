import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import CheerioSong,CheerioDance,Score,Match
from django.conf import settings
from pytz import timezone


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


def main_data(request):
    matches = Match.objects.all().order_by('updated_titme').reverse()
    result = []

    for match in matches.all():
        result.append({
            'name_kr': match.name_kr,
            'name_en': match.name_en,
            'score_kr': match.score_kr,
            'score_ys': match.score_ys,
            'updated_time': match.updated_titme.isoformat(),
        })
    result = json.dumps(result)

    return HttpResponse(result)
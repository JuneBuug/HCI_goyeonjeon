import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import CheerioSong,CheerioDance,Score,Match,Restaurant

from django.shortcuts import get_object_or_404,get_list_or_404


# Create your views here.

def song_list(request) :
    songs = get_list_or_404(CheerioSong)
    # songs = CheerioSong.objects.all()
    return render(request,'hci/song_list.html',{'songs': songs})

def dance_list(request) :
    dances = get_list_or_404(CheerioDance)
    return render(request,'hci/dance_list.html',{'dances': dances})

def main(request) :
    rests = get_list_or_404(Restaurant)
    matches = get_list_or_404(Match.objects.order_by('updated_titme').reverse())
    return render(request,'hci/main.html',{'matches':matches, 'rests': rests})

def history(request) :
    scores = get_list_or_404(Score)
    return render(request,'hci/history.html',{'scores':scores})


def main_data(request):
    matches = get_list_or_404(Match.objects.order_by('updated_titme').reverse())
    result = []

    for match in matches:
        result.append({
            'name_kr': match.name_kr,
            'name_en': match.name_en,
            'score_kr': match.score_kr,
            'score_ys': match.score_ys,
            'updated_time': match.updated_titme.isoformat(),
        })
    result = json.dumps(result)

    return HttpResponse(result)
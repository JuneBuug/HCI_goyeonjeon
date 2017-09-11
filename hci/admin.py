from django.contrib import admin
from .models import CheerioSong,CheerioDance,Scoring
# Register your models here.

admin.site.register(CheerioSong)
admin.site.register(CheerioDance)
admin.site.register(Scoring)
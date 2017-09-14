from django.contrib import admin
from .models import CheerioSong,CheerioDance,Score,Match
# Register your models here.

admin.site.register(CheerioSong)
admin.site.register(CheerioDance)
admin.site.register(Score)
admin.site.register(Match)

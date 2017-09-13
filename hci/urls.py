from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^song$', views.song_list, name='song_list'),
    url(r'^dance$',views.dance_list,name='dance_list'),
    url(r'^history$',views.history, name='history'),
    url(r'^$',views.main,name='main'),
]
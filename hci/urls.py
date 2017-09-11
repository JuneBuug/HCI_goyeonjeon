from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list$', views.song_list, name='song_list'),
    url(r'^$',views.main,name='main'),
]
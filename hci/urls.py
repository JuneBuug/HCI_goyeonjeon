from django.conf.urls import url
from . import views

app_name = 'hci'

urlpatterns = [
    url(r'^song$', views.song_list, name='song_list'),
    url(r'^dance$',views.dance_list,name='dance_list'),
    url(r'^history$',views.history, name='history'),
    url(r'^$',views.main,name='main'),
    url(r'^data$',views.main_data,name='main_data'),
]
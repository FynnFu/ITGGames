from django.conf.urls.static import static
from django.urls import path

from Home.views import *


urlpatterns = [
    path('', home, name="home"),
    path('page/<slug:slug>/', dynamic_page, name="dynamic_page"),
    path('games/', games, name="games"),
    path('genre/<slug:slug>/', genre, name="genre"),
    path('game/<slug:slug>/', game, name="game"),
    path('upload_game/<str:slug>', upload_images_game, name="upload_game"),
    path('upload_news/<str:slug>', upload_images_news, name="upload_news"),
    path('update_sequence_game/', update_sequence_game, name='update_sequence_game'),
    path('update_sequence_news/', update_sequence_news, name='update_sequence_news'),
    path('up_news/', up_update, name="up_update_news"),
    path('down_news/', down_update, name="down_update_news"),
    path('view_news/', view_news, name='mark_news_viewed'),
    path('news/<slug:slug>', news, name='news'),
]



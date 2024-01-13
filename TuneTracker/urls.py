
from django.urls import path
from TuneTracker import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('upload_song/', views.Addsong, name='upload_song'),
    path('artist_songs/', views.ArtistSongs, name='artist_songs'),
    path('song_detail/<int:pk>', views.song_detail, name='song_detail'),
    path('sucess_page/', views.success, name='sucess_page'),
    path('add_artist/', views.AddArtist, name='add_artist'),
]
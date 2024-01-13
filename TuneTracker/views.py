from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SongForm
from TuneTracker.models import Artist, Song
from django.http import JsonResponse

def HomeView(request):
    songs = Song.objects.all()
    return render(request, 'TuneTracker/home.html', {'songs':songs})

@csrf_exempt
def Addsong(request):
    """
    View for handling the song addition form submission.
    """
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/sucess_page')  # Redirect to a success page
    else:
        form = SongForm()

    return render(request, 'TuneTracker/upload_song.html', {'form': form})

def ArtistSongs(request):
    """
    View for rendering a page displaying the number of songs for each artist.
    """
    # Retrieves the list of all artists.
    artist_List = Artist.objects.all()
    # Counts the number of songs for each artist and stores it in a dictionary.
    song_count_dict = {}
    for a in artist_List:
        number_of_songs = Song.objects.filter(artist__name__icontains=a.name).count()
        song_count_dict[a.name] = number_of_songs

    return render(request, 'TuneTracker/artist_songs.html', {'song_count_dict':song_count_dict})
    
def song_detail(request, pk):
    """
    View for rendering the details of a specific song.
    """
    song = Song.objects.get(id=pk)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})

def success(request):
    return render(request, 'TuneTracker/sucess_page.html')

def AddArtist(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         artist_exists = Artist.objects.filter(name = name)
         if artist_exists:
         # If the artist already exists, returns a JSON response indicating the duplicate entry.
             return JsonResponse({'Already exits':'Artist name already exits'})
         
         # If valid, creates a new artist and redirects to the song addition page.
         artist = Artist.objects.create(name = name)
         return redirect('/upload_song')
    return render(request, 'TuneTracker/add_artist.html')
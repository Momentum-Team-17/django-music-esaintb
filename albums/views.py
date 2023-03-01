from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# take in requests and generate responses


def list_albums(request):
    albums = Album.objects.all()
    # goes to database and gets all instances of the model Album (djano ORM)
    # called a query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary


def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_albums.html', {'form': form})

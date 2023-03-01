from django.shortcuts import render
from .models import Album

# take in requests and generate responses


def list_albums(request):
    albums = Album.objects.all()
    # goes to database and gets all instances of the model Album (djano ORM)
    # called a query
    return render(request, 'albums/index.html', {'albums': albums})
    # pass data to the template using the context dictionary


def add_album(request):
    return render(request), 'albums/add_album.html'

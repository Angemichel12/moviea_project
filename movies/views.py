from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Movies
from django.shortcuts import get_object_or_404


def homepage(request):
	movies = Movies.objects.all()
	return render(request, 'index.html', {'movies': movies})
@login_required
def movieDetail(request, id):
	obj = get_object_or_404(Movies, pk=id)
	return render(request, 'movie_details.html',{'obj':obj})


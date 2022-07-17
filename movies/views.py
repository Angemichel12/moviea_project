from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def homepage(request):
	return render(request, 'index.html')
@login_required
def movieDetail(request):
	return render(request, 'movie-details.html')

# Create your views here.

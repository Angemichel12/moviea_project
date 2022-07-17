from django.urls import path
from .views import homepage, movieDetail


urlpatterns = [

	path('', homepage, name='home'),
	path('movie_detail/', movieDetail, name='detail')

]
from django.urls import path
from .views import homepage, movieDetail


urlpatterns = [

	path('', homepage, name='home'),
	path('<int:id>', movieDetail, name='detail'),

]
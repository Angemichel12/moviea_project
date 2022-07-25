from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movies(models.Model):
	title = models.CharField(max_length=100)
	released_date = models.DateField(default=timezone.now)
	length_time = models.CharField(max_length=3)
	description = models.TextField()
	trail_link = models.URLField(max_length = 200)
	movies_image = models.ImageField()
	rating = models.IntegerField(default=1)
	likes = models.ManyToManyField(User, related_name = 'blog_post')


	def __str__(self):
		return self.title

	
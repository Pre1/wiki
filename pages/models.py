from django.db import models
from django.urls import reverse
# Create your models here.
class Page(models.Model):
    title =  models.CharField(max_length=50)
    content =  models.TextField()
    last_update =  models.DateTimeField()

    def get_absolute_url(self):
    	# return "/detail/%i/" %(self.id)

    	return reverse('page-detail', kwargs={'page_id': self.id})


    def __str__(self):
    	return self.title
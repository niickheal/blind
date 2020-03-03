from django.db import models

def upload_feed_image(instance,filename):
	return "feed_images/{filename}".format(filename=filename)

class Feed(models.Model):
	headline = models.CharField(max_length=120)
	desc = models.CharField(max_length=500)
	def __str__ (self):
		return self.headline

class Books(models.Model):
	headline = models.CharField(max_length=120)
	desc = models.CharField(max_length=10000)
	def __str__ (self):
		return self.headline


from django.db import models

# Create your models here.
class urldata(models.Model):
	url=models.URLField(max_length=200)
	url_short=models.SlugField()

	"""docstring for urldata"models.Model """

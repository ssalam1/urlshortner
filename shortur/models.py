from django.db import models
from django import forms

# Create your models here.
class urldata(models.Model):
	url=models.CharField(max_length=200, null=False)
	url_short=models.SlugField(unique=True)

	"""docstring for urldata"models.Model """
class urlform(forms.ModelForm):
	"""docstring for urlfrom"""
	class Meta:
		model = urldata
		fields=['url']
		
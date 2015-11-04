from django.db import models

# Create your models here.
class urldata(models.Model):
	"""docstring for urldata"""
	url_id=models.IntegerField()
	big_url=models.CharField()
	short_url=models.CharField()
	def __init__(self, arg):
		super(urldata, self).__init__()
		self.arg = arg
		
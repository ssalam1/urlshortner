from django.contrib import admin
from shortur.models import *

# Register your models here.
class urldataAdmin(admin.ModelAdmin):
	"""docstring for urldataAdmin"""
	list_display = ('url','url_short')

admin.site.register(urldata, urldataAdmin)
		
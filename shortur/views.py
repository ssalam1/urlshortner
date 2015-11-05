from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.forms import ModelForm
from shortur.models import *
from random import randint
# Create your views here.
arr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def index(request):
	newurl=urldata()
	if request.method == "GET":
		form = urlform()
		return render (request, 'form.html',{'form':form})
	elif request.method == "POST":
		newurl.url=request.POST['url']
		newurl.url_short=shortner(newurl)
		newurl.save()
#		return HttpResponseRedirect('/index.html')
	return render_to_response ('done.html')

def shortner(newurl):
    id = randint(0,999999)
    n=id
    a=""
    while(n):
   	    a+=arr[n%62]
   	    n=n/62
    return a
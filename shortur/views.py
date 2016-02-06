from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.forms import ModelForm
from shortur.models import *
from random import randint
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.shortcuts import redirect
from django.contrib import messages 
import re
# Create your views here.
arr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def index(request):
    reg_exp_url = re.compile('^(?!mailto:)(?:(?:http|https|ftp)://)?(?:\\S+(?::\\S*)?@)?(?:(?:(?:[1-9]\\d?|1\\d\\d|2[01]\\d|22[0-3])(?:\\.(?:1?\\d{1,2}|2[0-4]\\d|25[0-5])){2}(?:\\.(?:[0-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-4]))|(?:(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)(?:\\.(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)*(?:\\.(?:[a-z\\u00a1-\\uffff]{2,})))|localhost)(?::\\d{2,5})?(?:(/|\\?|#)[^\\s]*)?$')
    newurl=urldata()
    if request.method == "GET":
        form = urlform()
        return render (request, 'form.html',{'form':form})
    elif request.method == "POST":
        if reg_exp_url.match(str(request.POST['url'])):
			newurl.url=request.POST['url']
			newurl.url_short=shortner(newurl)
			newurl.save()
			return render_to_response ('done.html',{'newurl':newurl})
        else: 
            messages.add_message(request, messages.INFO, 'Please Enter a Valid URL.')
            return redirect('/')

def shortner(newurl):
    id = randint(0,9999999)
    n=id
    a=""
    while(n):
   	    a+=arr[n%62]
   	    n=n/62
    return a
def notfound(request):
	return render_to_response('notfound.html')
def redirect_org(request,short_id):
	current_url= get_object_or_404(urldata,url_short=short_id) # get object, if not found return 404 error
 	orgurl=current_url.url
 	if orgurl[0:8] == 'https://' or orgurl[0:7]=='http://':
 		return redirect(orgurl)
 	else:
 		return redirect('https://'+orgurl)
  
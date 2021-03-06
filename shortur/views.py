from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.forms import ModelForm
from shortur.models import *
from random import randint
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.shortcuts import redirect
from django.contrib import messages 
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
# Create your views here.
arr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def index(request):
    newurl=urldata()
    if request.method == "GET":
        form = urlform()
        return render (request, 'form.html',{'form':form})
    elif request.method == "POST":
        val = URLValidator()
        try :
            val(request.POST['url'])
        except ValidationError, e : 
            messages.add_message(request, messages.INFO, e[0])
            return redirect('/')        
        newurl.url=request.POST['url']
        newurl.url_short=shortner(newurl)
        newurl.save()
        return render_to_response ('done.html',{'newurl':newurl})


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
 	return redirect(orgurl)
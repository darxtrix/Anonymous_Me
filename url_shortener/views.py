from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Template,Context
from django.core.context_processors import csrf

from url_shortener.models import URLtoHASH
from utils import hstring_to_id,hashed_string

import urllib,urlparse

from anonymous_me.settings.base import HOSTNAME


def home(request):
	context = Context({})
	context.update(csrf(request)) # it will lead to a post data form
	return render_to_response('index.html',context)

def shortify_url(request):
	if request.method == 'POST':
		context = Context({})
		url = request.POST.get('url','')

		if not url:
			context['errors'] = 'No URL was supplied' # checking for the supplied url if js is off
		else: # the url has been supplied
			try:
				check_obj = URLtoHASH.objects.get(url=url) # checking if the url is already shoretened or not
				hash_val = check_obj.hash_value
			except: # means the user entered a new url
				url_obj = URLtoHASH(url=url) # creating a new URL obj
				url_obj.save() # save to DB
				url_id = url_obj.id # getting the ID of the stored DB object
				hash_val = hashed_string(url_id)
				url_obj.hash_value = hash_val# saving the hashed value to the DB
				url_obj.save() # saving the changes to the DB


			shortened_url = urlparse.urlunparse(('http',HOSTNAME,hash_val,'','',''))
			context["success"] = shortened_url
			print shortened_url

		context.update(csrf(request))
		return render_to_response('index.html',context)


def redirect(request,hash_value):
	url_id = hstring_to_id(hash_value) # getting the ID of the url object in the DB
	url_obj = URLtoHASH.objects.get(id=url_id) # getting the url object from the url id
	if url_obj : 
		return HttpResponseRedirect(url_obj.url)
	else: # handle the case when the object is not in the DB
		context = Context({})
		context.update(csrf(request)) # since there will be a POST form 
		context['errors'] = 'No records found'
		return render_to_response('index.html',context)









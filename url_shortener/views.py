from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Template,Context
from django.core.context_processors import csrf

from url_shortener.models import URLtoHASH
from utils import shortify

import urlparse

from anonymous_me.settings.base import HOSTADDR


def home(request):
	context = Context({})
	context.update(csrf(request)) # it will lead to a post data form
	return render_to_response('index.html',context)

def shortify_url(request):
	if request.method == 'POST':
		context = Context({})
		url = request.POST.get('url','')

		if not url:
			context['errors'] = 'No URL was supplied'

		else:
			if not (url.startswith('http')):
				url = 'http://' + url
				print url
			(scheme,netloc,path,params,query,fragment) = urlparse.urlparse(url)
			# handle code for lower case andupper case urls
			# just need to change the domain name , then i'll do a url unparse
			try:
				check = URLtoHASH.objects.get(url=netloc) #returns a unique object
				new_path = check.hash_value
			except:
				url_entry = URLtoHASH(url=netloc)
				url_entry.save() #save to DB
				entry_id = url_entry.id
				new_path = shortify.hashed_string(entry_id)
				url_entry.hash_value = new_path
				url_entry.save()

			new_path = str(new_path) + path
			new_url = urlparse.urlunparse(('http',HOSTADDR,new_path,params,query,fragment))
			context["success"] = new_url
			print new_url

		context.update(csrf(request))
		return render_to_response('index.html',context)


def redirect(request):
	new_url = request.build_absolute_uri() # hashes are not sent to the server 
	(scheme,netloc,path,params,query,fragment) = urlparse.urlparse(new_url)
	path_list = path.split('/')
	hash_val = path_list[1]
	try:
		ob = URLtoHASH.objects.get(hash_value=hash_val)	 # will raise exception if the object does not exist			
		old_path = '/'.join(path_list[2:])
		orginal_url = urlparse.urlunparse((scheme,ob.url,old_path,params,query,fragment))
		print orginal_url
		return HttpResponseRedirect(orginal_url)

	except: # handle the case when the object is not in the DB
		context = Context({})
		context['errors'] = 'No records found'
		return render_to_response('index.html',context)









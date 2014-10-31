from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Template,Context
from django.core.context_processors import csrf

from url_shortener.models import URLtoHASH
from url_shortener import shortify

import urlparse


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
			print '####' + url
			(scheme,netloc,path,params,query,fragment) = urlparse.urlparse(url)
			# just need to change the domain name , then i'll do a url unparse
			try:
				check = URLtoHASH.objects.get(url=netloc) #returns a unique object
				new_domain_name = check.hash_value
			except:
				url_entry = URLtoHASH(url=netloc)
				url_entry.save()
				entry_id = url_entry.id
				new_domain_name = shortify.hashed_string(entry_id)
				url_entry.hash_value = new_domain_name
				url_entry.save()
				
			new_domain_name = 'http://localhost:8080/short/' + str(new_domain_name)
			new_url = urlparse.urlunparse((scheme,new_domain_name,path,params,query,fragment))
			context["success"] = new_domain_name
			print new_url

		context.update(csrf(request))
		return render_to_response('index.html',context)


def redirect(request,new_url):
	(scheme,netloc,path,params,query,fragment) = urlparse.urlparse(new_url)
	hash_val = path.split('/short/')[-1]
	try:
		ob = URLtoHASH.objects.get(hash_value=hash_val)
		context = Context({})
		context['errors'] = 'No records found'
		return render_to_response('index.html',context)
	except:
		orginal_url = urlparse.urlunparse((scheme,ob.url,path,params,query,fragment))
		return HttpResponseRedirect(orginal_url)









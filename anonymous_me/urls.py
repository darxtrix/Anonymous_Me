from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from url_shortener import views
from django.views.generic import TemplateView 

urlpatterns = patterns('',

    url(r'^$',views.home),
    url(r'^shortify_url$',views.shortify_url),
    url(r'^imankush/', include(admin.site.urls)),
    url(r'^google4962e1a518060429\.html$', lambda r: HttpResponse("google-site-verification: google4962e1a518060429.html", mimetype="text/plain")), #added google site ownership verification file
	url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')), #added ronots.txt file
	url(r'^sitemap.xml$',TemplateView.as_view(template_name='sitemap.xml')), #serving sitemap
    url(r'^(.*)$',views.redirect), # one more than one characters # .* matches everything

)

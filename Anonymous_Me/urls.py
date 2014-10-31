from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from url_shortener import views 

urlpatterns = patterns('',

    url(r'^$',views.home),
    url(r'^shortify_url$',views.shortify_url),
    url(r'^short/([a-zA-Z0-9]+)$',views.redirect),
    url(r'^admin/', include(admin.site.urls)),
)

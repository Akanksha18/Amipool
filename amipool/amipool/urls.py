from django.conf.urls import patterns, include, url
from amipool.views import hello, search_form, search, contact, thanks, gmap, aka

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', hello),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks),
    url(r'^map/$', gmap),
    url(r'^akanksha/$', aka),
    
    # url(r'^$', 'amipool.views.home', name='home'),
    # url(r'^amipool/', include('amipool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

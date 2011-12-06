from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^/?$', direct_to_template, {'template': 'home.html'}),
)

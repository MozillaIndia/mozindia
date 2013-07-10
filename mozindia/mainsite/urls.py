from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from . import views


urlpatterns = patterns('',
    url(r'^$', direct_to_template,
        {'template': 'mainsite/home.html'},
        name='mainsite.home'),
)

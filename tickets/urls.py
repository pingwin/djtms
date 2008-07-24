
from django.conf.urls.defaults import *

urlpatterns = patterns('tickets.views',
                       (r'^list[/]{0,1}(?P<action>[a-z]*)', 'list'),
                       (r'^list/(?P<action>[a-z]*)/(?P<orderby>[a-z_]*)/(?P<sortdir>[A-S]*)/$', 'list'),
                       (r'^create', 'create')
                       )
                       

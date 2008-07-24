from django.conf.urls.defaults import *

urlpatterns = patterns('projects.views',
#        (r'^list[/]{0,1}(?P<action>[a-z]*)', 'list'),
	(r'^list[/]{0,1}(?P<action>[a-z]*)[/]{0,1}(?P<orderby>[a-z_]*)[/]{0,1}(?P<sortdir>[A-S]*)', 'list'),

        (r'^create', 'create'),
        )

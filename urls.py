from django.conf.urls.defaults import *

# Uncomment this for admin:
# from django.contrib import admin

# Uncomment to load INSTALLED_APPS admin.py module for default AdminSite instance.
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/pingwin/www/django/project/templates/css/'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/pingwin/www/django/project/templates/js/'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/pingwin/www/django/project/templates/images/'}),

    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^projects/', include('projects.urls')),
    (r'^tickets/', include('tickets.urls')),
    
    (r'^(?P<file>.*)$', 'project.main.views.catchall'),
                       
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment this for admin docs:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment this for admin:
    # (r'^admin/(.*)', admin.site.root),
)

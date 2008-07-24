from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'accounts.views.index'),
	(r'^profile/$', 'accounts.views.profile'),
	(r'^signup/$', 'accounts.views.signup'),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'accounts/login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/accounts/login'}),

	(r'^changepassword/$', 'django.contrib.auth.views.password_change', {'template_name':'accounts/changePassword.html'}),
	(r'^changepassword/done/$', 'django.contrib.auth.views.password_change_done', {'template_name':'accounts/changePasswordDone.html'}),
	)
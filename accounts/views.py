from email_spammer.accounts.models import *

""" for all the auth models """
from django.contrib.auth.models import *

""" for HttpResponse """
from django.http import HttpResponseRedirect

""" for render_to_response """
from django.shortcuts import *

""" for login_required  """
from django.contrib.auth.decorators import *

""" for newforms """
from accounts.forms import *

from django.template import RequestContext
from django.contrib.auth import *


from main.functions import *

def index(request):
	return HttpResponseRedirect('/accounts/login/', {}, context_instance=RequestContext(request));


def detail(request, user_id):
	p = get_object_or_404(User, pk=user_id)
	return render('accounts/detail.html', {'user':p, 'request':request})

def signup(request):
	"""
	Sign a user up with our service.
	"""
	messages = []
	if request.POST:
		try:
			if not request.POST['password'] or request.POST['password'] != request.POST['password_confirm']:
				messages.append("Error: Passwords do not match");
				return render('accounts/signup.html', {'form':form, 'messages':messages, 'request':request})

			user = User.objects.create_user(
				request.POST['username'],
				request.POST['email'],
				request.POST['password']
				)

			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.is_active = True
			user.save()

			# must auth first
			new_user = authenticate(username=user.username, password=request.POST['password'])
			login(request, new_user)

			return HttpResponseRedirect("/accounts/profile/")
		except Exception, inst:
			if inst[0] == 1067:
				messages.append("Error: Duplicate Username")
			else:
				messages.append("Error: %s" % inst)
		form = ProfileForm(request.POST)
	else:
		form = ProfileForm()

	return render('accounts/signup.html', {'form':form, 'messages':messages, 'request':request})


@login_required
def profile(request):
	"""
	Manage the user Profile using ModelForm (only in development version of Django)
	"""
	if request.POST:
		form = ProfileForm(request.POST)

		if form.is_valid():
			form.save()
			#request.user.message_set.create(message="Failed to validate changes.")
			#return HttpResponseRedirect("/accounts/profile/")
	else:
		try:
			form = ProfileForm(instance=request.user)
		except SiteProfileNotAvailable:
			return HttpResponse("Unable to find profile")

	return render('accounts/profile.html', {'form' : form,'request':request})

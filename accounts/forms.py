from django.contrib.auth.models import User

from django.newforms import *

class ProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
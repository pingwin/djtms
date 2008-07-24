from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	activation_key = models.CharField(max_length=40)
	key_expires = models.DateTimeField()
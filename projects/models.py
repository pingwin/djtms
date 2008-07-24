from django.db import models
from project.tickets.models import *
from datetime import datetime


class Project(models.Model):
    """
    Model describing a project
    """
    date_created = models.DateTimeField('date created', core=True, default=datetime.now)
    name	 = models.CharField('project name', core=True, max_length=128)

    def __str__(self):
        return str(self.name)

    class Admin:
        pass


class MileStone(models.Model):
    """
    Model describing a milestone
    """
    date_created        = models.DateTimeField('date created', core=True, default=datetime.now)
    date_last_modified  = models.DateTimeField('date last modified', core=True, default=datetime.now)
    date_due	        = models.DateTimeField('date due', core=True, default=datetime.now)
    name 	        = models.CharField('milestone name', core=True, max_length=128)
    tickets		= models.ManyToManyField('Ticket')

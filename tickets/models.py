from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from project.projects.models import *

TICKET_STATUS = (
    (0, 'Closed'),
    (1, 'Open'),
    (2, 'Investigating'),
    (3, 'Under work'),
    (4, 'Rejected, see notes')
    )

TICKET_PRIORITY = (
    (0, 'Lowest'),
    (1, 'Low'),
    (2, 'Normal'),
    (3, 'High'),
    (4, 'Highest')
    )


class Ticket(models.Model):
    """
    A Ticket
    """
    date_created	= models.DateTimeField('date created', core=True, default=datetime.now)
    date_last_modified	= models.DateTimeField('date last modified', core=True, default=datetime.now)
    status		= models.IntegerField(core=True, choices=TICKET_STATUS, default=1)
    priority		= models.IntegerField(core=True, choices=TICKET_PRIORITY, default=2)
    author		= models.ForeignKey(User, related_name='authored_ticket')
    assigned		= models.ManyToManyField(User, related_name='assigned_ticket')
    subject		= models.CharField(core=True, max_length=128)
    contents		= models.TextField(core=True)
    projects		= models.ManyToManyField('Project')

    def __str__(self):
        return str(self.subject)

    class Admin:
        pass




class Comment(models.Model):
    """
    Ticket Comments
    """
    date_created	= models.DateTimeField('date created', core=True, default=datetime.now)
    author		= models.ForeignKey(User)
    ticket		= models.ForeignKey(Ticket)
    contents		= models.TextField(core=True)

    def __str__(self):
        return str(self.contents)

    class Admin:
        pass

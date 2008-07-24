from models import *
from django.forms import *

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('status', 'priority', 'project', 'assigned', 'subject', 'contents')


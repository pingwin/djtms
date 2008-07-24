from models import *
from forms import *
from main.functions import *
from projects.models import *

from django.contrib.auth.decorators import *

def list(request, action, orderby='date_created', sortdir='DESC'):
    
    resp = HttpResponse()
    resp.write('howdie')
    return resp




def create(request):
    	"""
	Create a new ticket
	"""
	if request.POST:
	
	        try:
			POST = request.POST.copy()

                	form = TicketForm(POST)

	                if form.is_valid():
        	        	t = Ticket(form.cleaned_data)
                		t.save()

                                if 'projects' in POST:
                                    for pid in POST['projects']:
                                        t.projects.add(pid)

                                    t.save()
                    
	   	                request.user.message_set.create(message="Ticket successfully created")
        		        return HttpResponseRedirect('/tickets/view/%d/' % t.id)

                        raise ValidationError(form.errors)
	        except ValidationError, inst:
                    	form = TicketForm(request.POST.copy())
                        request.user.message_set.create(message="Ticket Creation failed. '%s'" % inst)
        else:
            form = TicketForm()
        projects = Project.objects.all()

        return render('tickets/create.html', {'form':form, 'projects':projects, 'request':request})
            

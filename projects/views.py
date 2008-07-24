# Create your views here.

from models import *
from forms import *
from main.functions import *
from django.contrib.auth.decorators import *

from django.http import HttpResponse

@login_required
def list(request, action, orderby='date_created', sortdir='DESC'):
    """
    View the list of projects
    """
    try:
        if not orderby:
            orderby = 'date_created'
        if sortdir not in ['ASC', 'DESC']:
            sortdir = 'DESC'
        
        if action != 'mine':
	        projects = Project.objects.filter().order_by( orderby if sortdir == 'ASC' else '-'+str(orderby) )
        else:
            	projects = request.User.assigned_tickets_set.get().order_by( orderby if sortdir == 'ASC' else '-'+str(orderby) )

    except Project.DoesNotExist:
        projects = None

    except Exception, inst:
        resp = HttpResponse()
        resp.write(inst)
        return resp


    return render('projects/list.html', {'projects':projects, 'request':request})



@login_required
def create(request):
    """
    Create a new Project!
    """
    if request.POST:
        if len(request.POST['name']) > 6:
            p = Project(name=request.POST['name'])
            p.save()

            request.user.message_set.create(message='New Project Successfully created')

            if 'create_another' in request.POST:
	            return HttpResponseRedirect('/projects/create')

            return HttpResponseRedirect('/projects/list/%d/' % p.id)
    	else:
            request.user.message_set.create(message="Project name must be at least 6 chars")

    return render('projects/create.html', {'name':request.POST['name'] if 'name' in request.POST else '', 'request':request})

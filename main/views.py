# Create your views here.


from functions import *
from django.http import HttpResponse
from django.contrib.auth.decorators import *

@login_required
def catchall(request, file):
    resp = HttpResponse()
    try:
        for x in ['/', '|', ',', '.', '\\', '\'', '"']:
            if x in file:
                raise GenericError(404)

    	if not len(file):
            file = "index"
        
    	return render('main/%s.html' % file, {'request':request})
    except:
        raise Http404

    

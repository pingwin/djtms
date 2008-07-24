"""
Helper functions for quickly doing code the Brian Way.
"""
""" for render_to_response """
from django.shortcuts import *
from django.template import RequestContext

from django.http import HttpResponse




class GenericError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)




def pre(xx):
	"""
	Dump the contents of variable into a HttpResponse object and return the object.

	Intended code implemention is as follows

	---
	from main.functions import *
	def viewMethod(request):
		return dump(request)
	---
	"""
	resp = HttpResponse()
	resp.write( "<pre>"+str(xx)+"</pre>" )
	return resp




def render(tpl, vars=None):
	"""
	Shortcut function to short cut the render_to_response method.
	To push request variable context to the template just pass as
	element 'request' in the template vars dictionary list.
	"""
	if not vars:
		return render_to_response(tpl)

	if not vars['request']:
		return render_to_response(tpl, vars)

	return render_to_response(tpl, vars, context_instance=RequestContext( vars['request'] ))


def makeProperDomain(dn):
	"""
	Make a domain name proper with the trailing '.'
	"""
	numDots = dn.count('.')
	if not numDots or numDots > 2:
		return None

	if dn[ len(dn)-1 ] != '.':
		dn += '.'

	return dn

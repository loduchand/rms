# polls/views.py
from django.http import HttpResponse
from django.template.context_processors import request

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")



def rmsentry(request):
	return HttpResponse("<h1>welcome to drishti rms </h1>" + createFooter())


def createFooter():
	return "<b> this is the footer"
#from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Nonagon Media")

def detail(request, question_id):
	return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
	response = "The results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Vote on question %s" % question_id)



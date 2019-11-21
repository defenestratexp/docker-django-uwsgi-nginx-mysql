#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


# Create your views here.

# Example of a very simple view
#def index(request):
#    return HttpResponse("Welcome to Nonagon Media")

# This view displays the last 5 questions using the built-in
# database API to retrieve the info and uses a template to
# format the results
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
	response = "The results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Vote on question %s" % question_id)



from django.db import models

# For the date and timezone stuff to work
import datetime
from django.utils import timezone


# Create your models here.

# These come from the django polls tutoria
# Documentation is here: https://docs.djangoproject.com/en/2.2/intro/tutorial02/

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	# This method allows str translation of the object
	def __str__(self):
		return self.question_text

	# See if the item was created in the last day
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	# This method allows str translation of the object
	def __str__(self):
		return self.choice_text

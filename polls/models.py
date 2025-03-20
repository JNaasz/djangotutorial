import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateField("date published")
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


# in terminal to see objects in db:
# run `python manage.py shell` to enter interactive shell
# then run:
# from polls.models import Choice, Question
# Question.objects.all()
# Question.objects.filter(id=1)
# Question.objects.filter(question_text__startswith="What")
# from django.utils import timezone
# current_year = timezone.now().year
# Question.objects.get(pub_date__year=current_year)
# Question.objects.get(id=2) # may not exist
# Question.objects.get(pk=1) # primary key
# q = Question.objects.get(pk=1)
# q.was_published_recently()

#published_recently
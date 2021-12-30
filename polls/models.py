import datetime


import wallboard
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

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

class MakeRoute(models.Model):
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    mastery = models.IntegerField(default=0)
    difficulty = models.CharField(max_length = 3)
#    route = ArrayField(
#        ArrayField(
#            models.IntegerField(default=0),
#            size=40,
#        ),
#        size=21,
#    )

    route = ArrayField(ArrayField(models.IntegerField()))

    def __str__(self):
        return self.name


'''
import wallboard
from django.db import models
from polls.models import MakeRoute
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import numpy as np

a=[
    [2, 3],
    [2, 1],
])
route1 = MakeRoute(pub_date=timezone.now(), name="myroute", author="Oscar Hendrick", mastery=0, difficulty='v1', route=a)
route1.save()
route1.route()
'''

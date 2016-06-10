from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Neutri_User(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True, unique=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    username=models.CharField(max_length=200, unique=True)


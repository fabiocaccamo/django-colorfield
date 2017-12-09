#-*- coding: utf-8 -*-
from django.db import models
from colorfield.fields import ColorField


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

    

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    color = ColorField(default='#FF0000')
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.color

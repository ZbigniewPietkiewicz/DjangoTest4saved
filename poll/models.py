from django.db import models

# Create your models here.

class Poll(models.Model):
    poll_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

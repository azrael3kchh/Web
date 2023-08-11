"""
參照Django文檔
编写你的第一个 Django 应用，第 2 部分
測試class
cd mysite
python manage.py shell
from polls.models import Choice, Question
"""
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        """待補充"""
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """Choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

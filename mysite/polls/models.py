<<<<<<< HEAD
"""
參照Django文檔
编写你的第一个 Django 应用，第 2 部分
測試class
cd workspaces/Web/mysite
"""py
=======
'''
終端機測試
cd azrael3kchh/Web/mysite/mysite
'''
>>>>>>> 3c086f21d26fbde5919e256974eec7bdea924b38
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
<<<<<<< HEAD
        """待補充"""
        return self.question_text
    def was_published_recently(self):
        """待補充"""
=======
        return self.question_text
    def was_published_recently(self):
>>>>>>> 3c086f21d26fbde5919e256974eec7bdea924b38
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """Choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
<<<<<<< HEAD
        return self.choice_text
=======
        return self.choice_text
>>>>>>> 3c086f21d26fbde5919e256974eec7bdea924b38

from django.db import models

class Question(models.Model):
    question_text= models.CharField(max_length=255)
    pub_date = models.DateTimeField  ('date posted')

class Author(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

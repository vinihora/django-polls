import datetime

from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    CATEGORY = (
        ('Ciências', 'Ciências'),
        ('Matemática', 'Matemática'),
        ('História', 'História'),
        )

    categoria = models.CharField(max_length=200, null=True, choices=CATEGORY)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    who_created = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Customer,related_name = "like")
    dislike = models.ManyToManyField(Customer, related_name="dislike")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):

    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

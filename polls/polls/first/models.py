from django.db import models

class Questions(models.Model):
    text = models.CharField(max_length= 200)
    def __str__(self):
        return self.text

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    text = models.CharField(max_length= 200)
    votes = models.IntegerField(default= 0)
    def __str__(self):
        return self.text
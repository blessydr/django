from django.db import models

class star(models.Model):
    user_name=models.CharField(max_length=200)
    emai_l=models.EmailField()
    pass_word=models.IntegerField(max_length=10)
    
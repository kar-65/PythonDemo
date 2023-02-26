from django.db import models

# Create your models here.
class dolist(models.Model):
    name=models.CharField(max_length=250)
    prior=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name
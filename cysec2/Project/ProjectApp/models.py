from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ProjectCreate(models.Model):
    title = models.CharField(max_length=20)
    des = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

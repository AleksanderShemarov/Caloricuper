from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LastInfo(models.Model):

    title = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    team_staff = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.__class__.__name__} {self.title}"

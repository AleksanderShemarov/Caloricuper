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


class Developer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.ForeignKey(
        User, blank=True, null=True, related_name="nickname", on_delete=models.SET_NULL)
    born = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.TextField(max_length=150)
    telephones = models.TextField(blank=True, null=True, max_length=100)
    status_position = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

from django.db import models

# Create your models here.


class WeightIndexLevel(models.Model):
    category_number = models.CharField(max_length=50,
                                       help_text="a diapozone of weight indexes in numbers")
    category_name = models.CharField(
        max_length=50, help_text="name of a weight index diapozone")
    description = models.TextField(
        max_length=1000, help_text="a short description for a diapozone")

    def __str__(self):
        return self.category_name

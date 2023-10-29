from django.db import models


# Create your models here.
class Payment(models.Model):
    option = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.option

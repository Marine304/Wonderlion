from django.db import models

# Create your models here.
class Nanjang(models.Model):

    title = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.title

class Jujum(models.Model):

    title = models.CharField(max_length = 20)

    def __str__(self):
        return self.title
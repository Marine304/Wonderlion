from django.db import models
from taggit.managers import TaggableManager

class Nanjang(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    menu = models.ImageField(null=True, blank=True, upload_to='home/%Y/%m/%d')
    tags = TaggableManager()

    def __str__(self):
        return self.title

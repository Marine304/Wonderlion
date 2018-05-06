from django.db import models
from taggit.managers import TaggableManager

class Jujum(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)

    menu = models.ImageField(null=True, blank=True, upload_to='home/%Y/%m/%d')
    image1 = models.ImageField(null=True, blank=True, upload_to='home/%Y/%m/%d')
    image2 = models.ImageField(null=True, blank=True, upload_to='home/%Y/%m/%d')
    image3 = models.ImageField(null=True, blank=True, upload_to='home/%Y/%m/%d')

    tags = TaggableManager()
    like_count = models.IntegerField(default=0)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

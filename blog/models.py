from django.db import models

# Create your models here.
class Blog(models.Model):
    #author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

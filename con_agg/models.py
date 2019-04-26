from django.db import models

# Create your models here.

class WebsiteList(models.Model):
    web_name = models.CharField(max_length=50)
    web_url = models.CharField(max_length=300)


class Content(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    text = models.TextField()
    website = models.ForeignKey(WebsiteList, on_delete=models.CASCADE)

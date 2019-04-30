from django.db import models
from django.utils.timezone import now, datetime

# Create your models here.

class WebsiteList(models.Model):
    web_name = models.CharField(max_length=50)
    web_url = models.CharField(max_length=300)
    last_update = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.utcnow()
        return super(WebsiteList, self).save(*args, **kwargs)


    def __str__(self):
        return "{}, {}, and {}".format(self.web_name, self.web_url, self.last_update)

class Content(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    text = models.TextField()
    website = models.ForeignKey(WebsiteList, on_delete=models.CASCADE)

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
        return "{}".format(self.web_name)


class CreateContent(models.Manager):
    def create_content(self, title, article_url, website):
        content = self.create(title=title, article_url=article_url, website=website)
        return content


class Content(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=now())
    article_url = models.CharField(max_length=50)
    website = models.ForeignKey(WebsiteList, on_delete=models.CASCADE)

    objects = CreateContent()

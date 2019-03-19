from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=250)
    pubdate=  models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    def summary(self):
        return self.body[:500]

    def pub_date_pretty(self):\
        return self.pubdate.strftime('%b %e %Y')

    def __str__(self):
        return self.title
from django.db import models
# Create your models here.

class Infapp(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Blog(models.Model):
  title = models.CharField(max_length=100, blank=False, null=True, verbose_name='PAck title here', help_text='Please define your pack with a title')
  details = models.TextField(max_length=1000, blank=False, null=True, verbose_name='Pack notes here', help_text='Please take notes on your pack here')
  created_date = models.DateField(auto_now_add=True, auto_now=False)
  body = models.TextField()
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.title

  def summary(self):
    return self.body[:100]

  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y')
from __future__ import  unicode_literals
from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Guest(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    cell = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    zip = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    paper_file = models.FileField(null=True, blank=True,upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
  
    
    def __str__(self):
        return self.email

class AboutUs(models.Model): 
    title = models.CharField(max_length=200, default='About Us') 
    description = models.TextField(max_length=1000)
    picture = models.ImageField(null=True, blank=True,upload_to='images/',default='static/files/images/339c8096.jpg')

    
    def __str__(self):
        return self.title
  

class OurGoal(models.Model): 
    title = models.CharField(max_length=200, default='WHAT IS OUR GOAL?') 
    description = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    answer = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.answer

class FAQs(models.Model):
    question = models.CharField(max_length=200)
    answer = models.ManyToManyField(Answer)
    
    def __str__(self):
        return self.question
    
class EventTitles(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Location(models.MOdel):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects =models.GeoManager()
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Location"
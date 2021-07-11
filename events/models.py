from django.db import models

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
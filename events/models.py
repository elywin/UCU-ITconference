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

# class FAQs(models.Model):
#     question = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.question


class FAQs(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question


class Subquestions(models.Model):
    question       = models.CharField(FAQs, max_length=200, blank=True, null=True)
    answer         = models.CharField(max_length=200)
    subquestion    = models.ManyToManyField(FAQs, max_length=200, blank=True, null=False, through='Interconnector')
   
    def __str__(self):
        return str(self.question)

class Interconnector(models.Model):  # Interconnector for the two models
    faq          = models.ForeignKey(FAQs, on_delete=models.CASCADE)
    subquestion  = models.ForeignKey(Subquestions, on_delete=models.CASCADE)
    

    

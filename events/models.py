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


  
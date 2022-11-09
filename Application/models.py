from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank = True, null = True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name
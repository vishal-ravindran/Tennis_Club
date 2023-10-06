from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null= True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.firstName}  {self.lastName}"

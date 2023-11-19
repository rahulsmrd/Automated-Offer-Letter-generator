from django.db import models

# Create your models here.

class offerletter_data(models.Model):
    date_of_creation = models.DateTimeField(max_length=50)
    full_name=models.CharField(max_length=500)
    email=models.EmailField(max_length=500)
    course=models.CharField(max_length=100)
    join_date=models.DateField(max_length=50)
    end_date=models.DateField(max_length=50)
    unique_code=models.CharField(max_length=15,unique=True)
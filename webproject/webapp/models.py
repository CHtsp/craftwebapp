from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Courses(models.Model):
    key=models.IntegerField()
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    text=models.TextField()
    credit=models.CharField(max_length=20)
    img_path=models.CharField(max_length=150)


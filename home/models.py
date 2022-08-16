from django.db import models
class UserDataEnglish(models.Model):
    nguoiDung=models.CharField(max_length=100)
    ExerciseChoose=models.CharField(max_length=100)
    TopicChoose=models.TextField()

# Create your models here.

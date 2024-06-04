from django.db import models
# Create your models here.
class insuModel(models.Model):
    dummy_field = models.CharField(max_length=100)
    age=models.FloatField()
    bmi=models.FloatField()
    children=models.FloatField()
    sex_male=models.FloatField()
    smoker_yes=models.FloatField()

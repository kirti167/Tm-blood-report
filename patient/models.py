from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField(max_length=255)


class Patient(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    zip = models.IntegerField()

    def __str__(self):
        return f"{self.fname} {self.lname}"



class Document(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='media')
    def __str__(self):
        return self.name

class TestResult(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    value =models.FloatField()
    patient =models.ForeignKey(Patient,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.unit}"

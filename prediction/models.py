from django.db import models

# Create your models here.


class Breast_cancer(models.Model):
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.firstname + ": " + str(self.imagefile)

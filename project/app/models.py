from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    name = models.CharField(max_length = 50,verbose_name = "UserName")
    email = models.EmailField(verbose_name="UserEmail")
    contact = models.IntegerField()
    image = models.ImageField(upload_to="images/", height_field=None,width_field=None,max_length=100)
    # image = models.FileField(upload_to="images/",max_length=255)
    resume = models.FileField(upload_to="files/", max_length=254)
from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='Images/Upload')
    date = models.CharField(max_length=70)
    time = models.TimeField()
    position = models.CharField(max_length=70)


class Admin_User(models.Model):
    adminuser_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)


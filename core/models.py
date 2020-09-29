from django.db import models

# Create your models here.

class Services(models.Model):
    icon = models.ImageField(default='services.png')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ServicesTop(models.Model):
    service_header = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service_header[0:10]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    job_title = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name

class Banner(models.Model):
    img=models.ImageField()
    title=models.CharField(max_length=100, editable=False, default='banner')

    def __str__(self):
        return self.title
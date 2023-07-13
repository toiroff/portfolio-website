from django.db import models

# Create your models here.

class AboutMe(models.Model):
    information = models.TextField()
    projects  = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    happy_clients = models.CharField(max_length=200)
    customers = models.CharField(max_length=200)

class Skill(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class TimeLine(models.Model):
    duration = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.company

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='static/img')
    github = models.URLField()
    telegram = models.URLField()
    google = models.URLField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField()
    img = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

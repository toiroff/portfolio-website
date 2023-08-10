from django.db import models

# Create your models here.

class BotUser(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_id = models.CharField(max_length=200)
    body = models.CharField(max_length=3000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)


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
    photo = models.ImageField(upload_to='media')
    description = models.TextField()
    github = models.URLField(null=True,blank=True)
    project_url = models.URLField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField()


    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


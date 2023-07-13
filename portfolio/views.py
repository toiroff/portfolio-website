from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    about = AboutMe.objects.all()
    skill = Skill.objects.all()
    portfolio = Portfolio.objects.all()
    contact = Contact.objects.all()
    timeline = TimeLine.objects.all()
    blog = Blog.objects.all()
    ctg = {'about':about,'skill':skill,'portfolio':portfolio,'contact':contact,'timeline':timeline,'blog':blog}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('text')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('index')
    return render(request,'index.html',ctg)
from django.shortcuts import render
from django.template.context_processors import request
from .models import BuildJob
def index(request):
    jobs = BuildJob.objects.all()
    print jobs
    return render(request,'index.html',{'buildjobs':jobs})

def login(request):
    return render(request,'base.html')

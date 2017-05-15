from django.shortcuts import render
from django.template.context_processors import request
from jenkinsapi.jenkins import Jenkins
from .models import BuildJob
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


class JenkinsServerDetails(object):
    def __init__(self):
        return None

    def get_server_instance(self):
        jenkins_url = 'http://jenkins.ameyo.com:8080'
        server = Jenkins(jenkins_url, username='piyushjoshi', password='Piyu@cloud9*')
        return server


class BuildJobsDetails(object):
    serverInstance = None
    def __init__(self):
        return None
    
    def getAllBuildJobs(self):
        serverDetails = JenkinsServerDetails()
        self.serverInstance = serverDetails.get_server_instance()
        for job_name, job_instance in self.serverInstance.get_jobs():
             print 'Job Name:%s' % (job_instance.name)
             print "job namei si" + job_name
             print 'Job Description:%s' % (job_instance.get_description())
             print 'Is Job running:%s' % (job_instance.is_running())
             print 'Is Job enabled:%s' % (job_instance.is_enabled())
        return self.serverInstance.get_jobs()


def index(request):
    jobs = BuildJob.objects.all()
    print jobs
    paginator = Paginator(jobs,7)
    pageNumber = request.GET.get('page')

    try: 
        paginatedPage = paginator.page(pageNumber)
    except PageNotAnInteger: 
        pageNumber = 1
    except EmptyPage: 
        pageNumber = paginator.num_pages
    jobs = paginator.page(pageNumber)

    return render(request, 'index.html', {'buildjobs':jobs})

def login(request):
    return render(request, 'base.html')




from drms.drms import JenkinsServerDetails
class BuildJobsDetails(object):
    serverInstance = None
    def __init__(self):
        return ''
    
    def getAllBuildJobs(self):
        serverDetails = JenkinsServerDetails()
        self.serverInstance = serverDetails.get_server_instance()
        for job_name, job_instance in self.serverInstance.get_jobs():
             print 'Job Name:%s' % (job_instance.name)
             print 'Job Description:%s' % (job_instance.get_description())
             print 'Is Job running:%s' % (job_instance.is_running())
             print 'Is Job enabled:%s' % (job_instance.is_enabled()) 
        return None
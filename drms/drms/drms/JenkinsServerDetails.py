from jenkinsapi.jenkins import Jenkins


class JenkinsServerManager(object):
    def __init__(self):
        return ''

    def get_server_instance(self):
        jenkins_url = 'http://jenkins.ameyo.com:8080'
        server = Jenkins(jenkins_url, username='piyushjoshi', password='Piyu@cloud9*')
        return server

    if __name__ == '__main__':
        print get_server_instance().version
    
    

import json
from urllib import urlencode
from urllib3 import RequestWithMethod
from urllib2 import Request, urlopen, URLError

class circleAPI:
    key = None
    base_url = None

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url

    def get(self, url):
        request = Request(url, headers={'Accept' : 'application/json'})
        try:
            response = urlopen(request)
            data = response.read()
            return data
        except URLError, e:
            print("Uh oh, something went horribly wrong...")
            print e
            return None

    def delete(self, url):
        request = RequestWithMethod('DELETE', url, headers={'Accept' : 'application/json'})
        try:
            response = urlopen(request)
            data = response.read()
            return data
        except URLError, e:
            print("Uh oh, something went horribly wrong...")
            print e
            return None

    def post(self, url, tup):
        tup = json.dumps(tup)
        print tup
        request = Request(url, headers={'Accept' : 'application    /json', 'Content-Type': 'application/json'})
        try:
            response = urlopen(request, tup)
            data = response.read()
            return data
        except URLError, e:
            print("Uh oh, something went horribly wrong...")
            print e
            return None

    def getProjects(self):
        request = self.get(self.base_url + "/api/v1/projects?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def getBuilds(self, username, reponame):
        request = self.get(self.base_url + "/api/v1/project/" + username + "/" + reponame + "?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def getEnvironmentVariables(self, username, reponame):
        request = self.get(self.base_url + "/api/v1/project/" + username + "/" + reponame + "/envvar?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def deleteEnvironmentVariable(self, username, reponame, envvar):
        request = self.delete(self.base_url + "/api/v1/project/" + username + "/" + reponame + "/envvar/" + envvar + "?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def addEnvironmentVariable(self, username, reponame, tup):
        request = self.post(self.base_url + "/api/v1/project/" + username + "/" + reponame + "/envvar?circle-token=" + self.key, tup)
        print request
        data = json.loads(request)
        return data

    def getSingleBuild(self, username, reponame, buildNum):
        request = self.get(self.base_url +"/api/v1/project/" + username + "/" + reponame + "/" + buildNum + "?circle-token=" + self.key)
        data = json.loads(request)
        return data

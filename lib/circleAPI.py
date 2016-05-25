import json
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

    def getProjects(self):
        request = self.get("https://circleci.com/api/v1/projects?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def getBuilds(self, username, reponame):
        request = self.get("https://circleci.com/api/v1/project/" + username + "/" + reponame + "?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def getEnvironmentVariables(self, username, reponame):
        request = self.get("https://circleci.com/api/v1/project/" + username + "/" + reponame + "/envvar?circle-token=" + self.key)
        data = json.loads(request)
        return data

    def getSingleBuild(self, username, reponame, buildNum):
        request = self.get("https://circleci.com/api/v1/project/" + username + "/" + reponame + "/" + buildNum + "?circle-token=" + self.key)
        data = json.loads(request)
        return data

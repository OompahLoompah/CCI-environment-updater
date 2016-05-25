import yaml
from lib.circleAPI import circleAPI

f = open ('.config')
config = yaml.load(f)
key = config['api_key']
base_url = config['base_url']

circle = circleAPI(key, base_url)
projects = circle.getProjects()

var = "seanfoo"
value = "hahaha!"
tup = {"name": "seanfoo", "value":"hahaha!"}
for project in projects:
    envvars = circle.getEnvironmentVariables(project['username'], project['reponame'])
    for envvar in envvars:
        if envvar['name'] == var:
            print project['username'] + "/" + project['reponame']
            circle.deleteEnvironmentVariable(project['username'], project['reponame'], var)
            circle.addEnvironmentVariable(project['username'], project['reponame'], tup)

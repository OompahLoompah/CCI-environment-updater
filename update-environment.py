import yaml
import sys
import time
from lib.circleAPI import circleAPI
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-k", "--key", action="store", help="Environment variable name to check for")
parser.add_option("-v", "--value", action="store", help="New value to assign to variable")
options, args = parser.parse_args()

if not options.key:   # if filename is not given
    parser.error('Envvar key not given')

if not options.value:   # if filename is not given
    parser.error('New value not given')

f = open ('.config')
config = yaml.load(f)
key = config['api_key']
base_url = config['base_url']

circle = circleAPI(key, base_url)
projects = circle.getProjects()

var = options.key
value = options.value
tup = {"name": var, "value": value}
for project in projects:
    envvars = circle.getEnvironmentVariables(project['username'], project['reponame'])
    for envvar in envvars:
        if envvar['name'] == var:
            print project['username'] + "/" + project['reponame']
            circle.deleteEnvironmentVariable(project['username'], project['reponame'], var)
            circle.addEnvironmentVariable(project['username'], project['reponame'], tup)
            time.sleep(2) #To prevent us from hammering the API too hard

# CCI-environment-updater
This script checks for projects with builds that have used a given environment variable and uses the CircleCI API to update the variable to a new value. This can be configured to be used on either circleci.com or on CircleCI Enterprise.

##Caveats

This script will only update environment variables of projects you are following. If you have any user who is following all of your projects you should use their API key when running this.

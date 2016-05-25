# CCI-environment-updater
This script checks for projects with builds that have used a given environment variable and uses the CircleCI API to update the variable to a new value. This can be configured to be used on either circleci.com or on CircleCI Enterprise.

##Use

First edit .config-example and add your api key and base url in place of the existing example values.

then run 

`python update-environment.py -k <someVarName> -v <someValue>`

where `<someVarName>` is the name of the variable you are replacing and `<someValue>` is the new value you want

##Caveats

This script will only update environment variables of projects you are following. If you have any user who is following all of your projects you should use their API key when running this.

Additionally, this script has the ability to delete environment variables which is a destructive operation and can cause problems if it's interrupted after deleting the original but before adding a new variable. If this happens check the script's output for the last repo that was printed and then manually add the new variable to that repo.

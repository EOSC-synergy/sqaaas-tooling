#!/usr/local/bin/python
from github import Github
from github import GithubException
import sys

g = Github()
# In case an access token is needed
#g = Github("access_token")

repo = g.get_repo(sys.argv[1])
try:
    license = repo.get_license()
    print("Found license for repository %s: %s" %(repo.name,license.license))
except GithubException:
    print("License not found in repository")
        

#!/usr/local/bin/python
from github import Github
from github import GithubException
import sys

def isLicenseFilePresent(repo):
    try:
        license = repo.get_license()
        print("Found license for repository %s: %s" %(repo.name,license.license))
        return True
    except GithubException:
        print("License not found in repository")
        return False

g = Github()

repo = g.get_repo(sys.argv[1])
assert(isLicenseFilePresent(repo))


from github import Github
from github import GithubException
from urllib.parse import urlparse
import gitlab
import sys

def isLicensePresentGithub(url):
    g = Github()
    repo = g.get_repo(url)
    try:
        license = repo.get_license()
        print("Found license for repository %s: %s" %(repo.name,license.license))
        return True
    except GithubException:
        print("License not found in repository")
        return False

def isFileInGitlabRepo(server,repo,file):
    gl = gitlab.Gitlab(server)
    project = gl.projects.get(repo)
    items = project.repository_tree()
    for item in items:
        if(item['name'] == file):
            print("File %s found in Gitlab repository %s"%(file,repo))                        
            return True
    print("File %s not found in Github repository %s"%(file,repo))
    return False

#g = Github()

#repo = g.get_repo(sys.argv[1])

def isLicenseFilePresent(url):
    o = urlparse(url)
    repo = o.path[1:]
    if(o.hostname == 'github.com'):        
        return isLicensePresentGithub(repo)
    else:
        server = o.scheme + "://" + o.netloc
        return isFileInGitlabRepo(server,repo,'LICENSE')


url = sys.argv[1]
print("Repository URL " , url)
assert(isLicenseFilePresent(url))



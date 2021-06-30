from github import Github
from github import GithubException
from urllib.parse import urlparse
import gitlab
import sys

def is_license_present_github(url):
    g = Github()
    g_repo = g.get_repo(url)
    try:
        repo_license = g_repo.get_license()
        print("Found license for repository %s: %s" %(g_repo.name,repo_license.license))
        return True
    except GithubException:
        print("License not found in GitHub repository")
        return False

def is_file_in_gitlab_repo(server,repo,file):
    gl = gitlab.Gitlab(server)
    try:
        project = gl.projects.get(repo)
        items = project.repository_tree()
        for item in items:
            if(item['name'] == file):
                print("File %s found in GitLab repository %s"%(file,repo))                        
                return True
    except gitlab.exceptions.GitlabGetError:
        print("Repository not found or no permission to access it. ")
        return False
    print("File %s not found in GitLab repository %s"%(file,repo))
    return False


def is_license_file_present(url):
    o = urlparse(url)
    repo = o.path[1:]
    if(o.hostname == 'github.com'):        
        return is_license_present_github(repo)
    else:
        server = o.scheme + "://" + o.netloc
        return is_file_in_gitlab_repo(server,repo,'LICENSE')


url = sys.argv[1]
print("Repository URL " , url)
assert(is_license_file_present(url))



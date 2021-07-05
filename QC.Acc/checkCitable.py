from github import Github
from github import GithubException
from urllib.parse import urlparse
import gitlab
import sys



def is_file_in_github_repo(repo,file):
    g = Github()
    g_repo = g.get_repo(repo)
    try:
        g_repo.get_contents(file)
        print("File %s found in GitHub repository %s"%(file,g_repo.name))
        return True
    except GithubException:
        print("File %s not found in GitHub repository %s"%(file,g_repo.name))
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
        print("Repository not found or no permission to access it.")
        return False
    print("File %s not found in GitLab repository %s"%(file,repo))
    return False

def is_file_in_repo(url,file):
    o = urlparse(url)
    repo = o.path[1:]
    if(o.hostname == 'github.com'):        
        return is_file_in_github_repo(repo,file)
    else:
        server = o.scheme + "://" + o.netloc
        return is_file_in_gitlab_repo(server,repo,file)


url = sys.argv[1]
print("Repository URL " , url)
assert (is_file_in_repo(url,"CITATION.json") or is_file_in_repo(url,"codemeta.json"))



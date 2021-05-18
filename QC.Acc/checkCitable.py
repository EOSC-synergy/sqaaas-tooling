from github import Github
from github import GithubException
from urllib.parse import urlparse
import gitlab
import sys



def isFileInGithubRepo(repoPath,file):
    g = Github()
    repo = g.get_repo(repoPath)
    try:
        repo.get_contents(file)
        print("File %s found in Github repository %s"%(file,repo.name))
        return True
    except GithubException:
        print("File %s not found in Github repository %s"%(file,repo.name))
        return False

def isFileInGitlabRepo(server,repo,file):
    gl = gitlab.Gitlab(server)
    try:
        project = gl.projects.get(repo)
        items = project.repository_tree()
        for item in items:
            if(item['name'] == file):
                print("File %s found in Gitlab repository %s"%(file,repo))                        
                return True
    except gitlab.exceptions.GitlabGetError as e:
        print("Repository not found or no permission to access it. ")
        return False
    print("File %s not found in Github repository %s"%(file,repo))
    return False

def isFileInRepository(url,file):
    o = urlparse(url)
    repo = o.path[1:]
    if(o.hostname == 'github.com'):        
        return isFileInGithubRepo(repo,file)
    else:
        server = o.scheme + "://" + o.netloc
        return isFileInGitlabRepo(server,repo,file)


url = sys.argv[1]
print("Repository URL " , url)
assert((isFileInRepository(url,"CITATION.json") or isFileInRepository(url,"codemeta.json")))



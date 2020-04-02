import analyseGithub

def test_containsGithubURL_empty():
    assert not analyseGithub.containsGitHubURL("")

def test_containsGithubURL_noUrl():
    assert not analyseGithub.containsGitHubURL("Some test tweet")

def test_containsGithubURL_url():
    repo = "https://github.com/git/git"
    assert analyseGithub.containsGitHubURL(repo)

def test_extractGitHubLink():
    repo = "git/git"
    assert analyseGithub.extractGitHubLink("https://github.com/{repo} more tweet") == repo

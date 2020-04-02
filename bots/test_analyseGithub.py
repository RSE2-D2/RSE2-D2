import analyseGithub

def test_containsGithubURL_empty():
    assert analyseGithub.containsGitHubURL("") == False

def test_containsGithubURL_noUrl():
    assert analyseGithub.containsGitHubURL("Some test tweet") == False

def test_containsGithubURL_url():
    assert analyseGithub.containsGitHubURL("https://github.com/git/git") == True

def test_extractGitHubLink():
    assert analyseGithub.extractGitHubLink("https://github.com/git/git more tweet") == "git/git"

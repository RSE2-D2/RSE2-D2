import analyseGithub

def test_containsGithubURL_empty():
    assert not analyseGithub.containsGitHubURL("")

def test_containsGithubURL_noUrl():
    assert not analyseGithub.containsGitHubURL("Some test tweet")

def test_containsGithubURL_url():
    repo = "https://github.com/git/git"
    assert analyseGithub.containsGitHubURL(repo)

def test_extractGitHubLink():
<<<<<<< HEAD
    assert analyseGithub.extractGitHubLink("https://github.com/git/git more tweet") == "git/git"
=======
    repo = "https://github.com/git/git"
    assert analyseGithub.extractGitHubLink(f"{repo} more tweet") == repo
>>>>>>> 4e7007bb958a62bf9483ff7f77c3641d2482f3e9

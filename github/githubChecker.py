from github import Github

### Filenames we want to see present
files_we_need = {
    "readme" : ["readme", "README", "README.md", "readme.md",
"readme.rst", "README.rst"]
}

###


# TODO read in token
g = Github("tokenhere")

# TODO replace with code that reads in the repo url and snips out the org and repo
repo_name = "RSE2-D2/RSE2-D2"

# fetch the repo details from GitHub
repo = g.get_repo(repo_name)

# gather all files in the root of the repo
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

print(files_we_need["readme"])

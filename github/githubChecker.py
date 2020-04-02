from github import Github

### Filenames we want to see present
# To add another file type use this template schema
#     "filetypeDescription" : {
#        "filenames" : ["file.md", "FILE", "permutation3"],
#        "error" : "errorname_from_advice_db.json"
#    }


files_we_need = {
    "readme" : {
    "filenames" : ["readme", "README", "README.md", "readme.md",
"readme.rst", "README.rst"],
    "error" :"NoReadMe"
    },
    "licence" : {
        "filenames" : [],
        "error" : ""
    }
}

###


# TODO read in token
g = Github("0114ca588dbbab455af6f021d612b3466e34583f")

# TODO replace with code that reads in the repo url and snips out the org and repo
repo_name = "RSE2-D2/RSE2-D2"

# fetch the repo details from GitHub
repo = g.get_repo(repo_name)

# gather all files in the root of the repo
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

print(files_we_need["readme"])

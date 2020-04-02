from github import Github

### Filenames we want to see present
# To add another file type use this template schema
#     "filetypeDescription" : {
#        "filenames" : ["file.md", "FILE", "permutation3"],
#        "error" : "errorname_from_advice_db.json"
#    }


files_we_need = { #Use casefold() for case insensitive comparison 
    "readme" : {
    "filenames" : ["readme", "readme.md", "readme.rst", "readme.txt"],
    "error" :"NoReadMe"
    },
    "license" : {
        "filenames" : ["license", "license.md", "license.rst", "license.txt"],
        "error" : "NoLicense""
    },
    "codeofconduct" : {
        "filenames" : ["code_of_conduct", "codeofconduct", "code_of_conduct.md", "codeofconduct.md", "code_of_conduct.rst", "codeofconduct.rst"  "code_of_conduct.txt", "codeofconduct.txt"],
        "error" : "NoCodeOfConduct""
    }
# Add more files from https://github.com/joelparkerhenderson/github_special_files_and_paths ?
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

print(files_we_need["readme", "license", "codeofconduct"])

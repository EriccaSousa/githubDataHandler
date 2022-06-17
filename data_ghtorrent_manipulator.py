from github import Github
import github
import json
import os

import file_handler

token = os.environ['TOKEN_GITHUB']
github = Github(token)

def search_all_commits_by_repository_name(name_project):
    try:
        repository = github.search_repositories(query=f"{name_project}in:name")[0]

        commits = repository.get_commits()

        for commit in commits:
            file_handler.write_csv(commit.html_url, commit.commit.message)
    except IndexError:
                print(f"list index out of range")

def read_json():
    with open("resource\GHTorrent\Projetos\Projetos_Candidatos_FrontEstruturas.json", encoding='utf-8') as projetos_candidatos:
        projetos = json.load(projetos_candidatos)

    for i in projetos:
        name_project = i['name']
        search_all_commits_by_repository_name(name_project)

read_json()
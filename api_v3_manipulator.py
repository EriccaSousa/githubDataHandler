from github import Github
import requests
import os

import csv_manipulator

token = os.environ['TOKEN_GITHUB']
headers = {'Authorization': f'token {token}'}

def search_respositories_by_topic(topic):
    github = Github(token)
    headers = {'Authorization': f'token {token}'}

    print("Step 1 - Buscando repositórios")
    repositories = github.search_repositories(query=f"{topic}in:name,description,topic")
    print("Total de repositórios encontrados: ") 
    print(repositories.totalCount)

    print("Step 2 - Buscando todos os commits dos repositórios candidatos")
    print("Salvando commits candidatos em arquivo csv")
    for i in repositories:
        i.get_commits().totalCount;
        search_commits_by_repo_cadidates(i.owner.login, i.name, i.url, headers)

def search_commits_by_repo_cadidates(repo_owner, repo_name, repo_url, headers):
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits", headers=headers)

    response_data = response.json()

    for i in range(len(response_data)):
        try:
            csv_manipulator.write_csv(repo_name, repo_url, response_data[i]["html_url"], response_data[i]["commit"]["message"])
        except KeyError:
            var = 0
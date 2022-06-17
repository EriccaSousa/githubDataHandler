from github import Github
import github
import os

import file_handler

token = os.environ['TOKEN_GITHUB']
github = Github(token)

def search_respositories_by_topic(topic):
        print("BUSCANDO REPOSITÓRIOS")
        repositories = github.search_repositories(query=f"{topic}in:name,description,topic")
        
        search_all_commits_by_repository(repositories)

def search_all_commits_by_repository(repositories):
    for repo in repositories:
            commits = repo.get_commits()
            print("----------------------------------------------------------------------")
            print(f"VERIFICANDO SE REPOSITÓRIO {repo.name} ATENDE AOS REQUISITOS")
            try:
                if(commits.totalCount > 100):
                    print(f"repositório {repo.name} atende aos requisitos")
                    print(f"EXTRAINDO COMMITS")
                    print(f"Total de commits a serem extraídos: {commits.totalCount}")
                    for commit in commits:
                        file_handler.write_csv(commit.html_url, commit.commit.message)
                else:
                    print(f"Repositório {repo.name} não atende aos requisitos")
            except github.GithubException:
                print(f"Erro desconhecido ao acessar repositório {repo.name}")

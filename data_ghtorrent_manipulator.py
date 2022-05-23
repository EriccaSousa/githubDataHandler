import json
import csv
import requests
import os

token = os.environ['TOKEN_GITHUB']
headers = {'Authorization': f'token {token}'}

def buscar_dados(url_project, headers):
    response = requests.get(url_project + "/commits", headers=headers)

    response_data = response.json()
    print("Extraindo commits do projeto: " + url_project)
    for i in range(len(response_data)):
        try:
            write_csv(url_project, response_data[i]["html_url"], response_data[i]["commit"]["message"])
        except KeyError:
            var = 0

def write_csv(url_project, url_commit, message):
    with open('resource\GHTorrent\Commits\commits_candidatos_robot.csv', mode='a', newline='', encoding="utf-8") as csv_file:
        field_names = ["url_project", "url_commit", "message"]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=';')

        #writer.writeheader()
        writer.writerow({"url_project": url_project, "url_commit": url_commit, "message": message})

def read_json():
    print("Lendo projetos candidatos")
    with open("resource\GHTorrent\Projetos\Projetos_Candidatos_Robot.json", encoding='utf-8') as projetos_candidatos:
        projetos = json.load(projetos_candidatos)

    print("Extraindo commits e salvando em arquivo csv")
    for i in projetos:
        url_project = i['url']
        buscar_dados(url_project, headers)

read_json()

import csv

def write_csv(repo_name, repo_url, url_commit, message):
    with open('resource\GitHub\Commits\Commits_Candidatos_Cypress.csv', mode='a', newline='', encoding="utf-8") as csv_file:
        field_names = ["repo_name", "repo_url", "url_commit", "message"]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=';')

        #writer.writeheader()
        writer.writerow({"repo_name": repo_name, "repo_url": repo_url, "url_commit": url_commit, "message": message})
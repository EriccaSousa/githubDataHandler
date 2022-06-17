import json
import csv

def write_csv(url_commit, message):
    with open('resource\GHTorrent\Commits\commits_candidatos_frontestruturas.csv', mode='a', newline='', encoding="utf-8") as csv_file:
        field_names = ["url_commit", "message"]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=',')

        #writer.writeheader()
        writer.writerow({"url_commit": url_commit, "message": message})
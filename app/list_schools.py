import requests
from bs4 import BeautifulSoup
import csv
from IPython import embed

schools = []

def clean_href(href):
    return href.replace("\\", "").strip("\"")

if __name__ == "__main__":

    with open("mocks/disclosures_div.html", "r") as html_file:
        document = html_file.read()
        soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning when parsing local file
        links = soup.find_all("a") # around 215 items
        for link in links:
            name = link.text
            if not name in ["Standard 509 Information Reports", "Employment Summary Reports", ""]:
               schools.append({"name": name, "url": clean_href(link.attrs["href"])})

    with open("data/schools.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "url"])
        writer.writeheader() # uses fieldnames set above

        for school in schools:
            print(school)
            writer.writerow(school)

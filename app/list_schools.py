import requests
from bs4 import BeautifulSoup
import csv
import re
from IPython import embed

schools = []

def clean_href(href):
    return href.replace("\\", "").strip("\"")

#def clean_name_part(name_part):
#    name_part = name_part.replace(")","")
#    return name_part.strip().upper()
#
#def clean_name(name):
#    name_parts = name.split("(")
#    name_parts = list(map(clean_name_part, name_parts))
#    return name_parts[0] #, name_parts[-1]

def clean_name(name):
    starting_index_of_last_paren = [m.start() for m in re.finditer("\(", name)][-1] # adapted from source: https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
    name = name[0:starting_index_of_last_paren] # use everything before the last paren begins
    return name.strip().upper()

if __name__ == "__main__":

    with open("mocks/disclosures_div.html", "r") as html_file:
        document = html_file.read()
        soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning when parsing local file
        links = soup.find_all("a") # around 215 items
        for link in links:
            if not link.text in ["Standard 509 Information Reports", "Employment Summary Reports", ""]:
                schools.append({"name": clean_name(link.text), "url": clean_href(link.attrs["href"])})

    with open("data/schools.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "url"])
        writer.writeheader() # uses fieldnames set above

        for school in schools:
            print(school)
            writer.writerow(school)

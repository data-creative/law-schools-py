import requests
from bs4 import BeautifulSoup
import csv
import re
from IPython import embed

schools = []

def clean_href(href):
    return href.replace("\\", "").strip("\"")

def index_of_last_open_paren(text):
    return [m.start() for m in re.finditer("\(", text)][-1] # adapted from source: https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python

def index_of_last_close_paren(text):
    return [m.start() for m in re.finditer("\)", text)][-1] # todo: refactor

def parse_link_text(text):
    o = index_of_last_open_paren(text)
    c = index_of_last_close_paren(text)

    name = text[0 : o] # use everything before the last paren begins
    name = name.strip().upper()

    year = text[o+1:c] # use everything between the last parens
    try:
        year = int(year)
    except ValueError as e: # handle when there is other text in the year (a hyphen) todo: refactor
        i = year.index("-")
        year = year[i+1 :].strip() # use everything after the last hyphen, inclusive
        try:
            year = int(year)
        except ValueError as e: # handle when there is other text in the year (a semi-colon) todo: refactor
            s = year.index(";")
            year = year[s+1 :].strip()
            year = int(year)

    return name, year

if __name__ == "__main__":

    with open("mocks/disclosures_div.html", "r") as html_file:
        document = html_file.read()
        soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning when parsing local file
        links = soup.find_all("a") # around 215 items
        for link in links:
            if not link.text in ["Standard 509 Information Reports", "Employment Summary Reports", ""]:
                name, year = parse_link_text(link.text)
                url = clean_href(link.attrs["href"])
                schools.append({"name": name, "year": year, "url": url})

    with open("data/schools.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "year", "url"])
        writer.writeheader()

        for school in schools:
            print(school)
            writer.writerow(school)

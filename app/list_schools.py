import requests
from bs4 import BeautifulSoup
import csv
import re
import json
from IPython import embed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def request_html():
    URL = "https://www.americanbar.org/groups/legal_education/resources/aba_approved_law_schools/official-guide-to-aba-approved-law-schools.html"
    driver = webdriver.Firefox()
    driver.get(URL)
    tables = driver.find_elements_by_tag_name("table")
    table = [table for table in tables if ("AKRON (1961)" in table.text and "YALE (1923)" in table.text)][0]
    table_html = table.get_attribute('innerHTML')
    driver.close() # important, closes browser
    return table_html

def parse_html(document):
    soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning
    links = soup.find_all("a") # around 215 items
    schools = []
    for link in links:
        if not link.text in ["Standard 509 Information Reports", "Employment Summary Reports", ""]:
            name, year = parse_link_text(link.text)
            url = link.attrs["href"]
            schools.append({"name": name, "year": year, "url": url})
    return schools

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

    document = request_html()

    # writing this HTML output to file enables further dev and testing without re-requesting each time.
    # ... also, FYI - if new content is written to file, tests might need updating (this is desired).
    with open("mocks/schools_tbody.html", "w") as html_file:
        html_file.write(document)

    schools = parse_html(document)

    with open("data/schools.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "year", "url"])
        writer.writeheader()

        for school in schools:
            print(school)
            writer.writerow(school)

    with open("data/schools.json", "w") as json_file:
        json_file.write(json.dumps(schools))

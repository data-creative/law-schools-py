import requests
from bs4 import BeautifulSoup
from IPython import embed

school_links = []

with open("mocks/disclosures_div.html", "r") as file:
    document = file.read()

    soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning when parsing local file

    links = soup.find_all("a") # around 215 items

    for link in links:
        # not if text == "" or text in ['Standard 509 Information Reports', ]
        text = link.text #> 'Standard 509 Information Reports'
        href = link.attrs["href"] #> '\\"http://www.abarequireddisclosures.org/\\"'
        school_links.append({"school": text, "url": href})

for school_link in school_links:
    print(school_link)

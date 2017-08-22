import requests
from bs4 import BeautifulSoup
from IPython import embed

school_links = []

def clean_href(href):
    return href.replace("\\", "").strip("\"")

if __name__ == "__main__":

    with open("mocks/disclosures_div.html", "r") as file:
        document = file.read()

        soup = BeautifulSoup(document, "lxml") # use "lxml" param to avoid warning when parsing local file

        links = soup.find_all("a") # around 215 items

        for link in links:
            # not if text == "" or text in ['Standard 509 Information Reports', ]
            school_links.append({"school": link.text, "url": clean_href(link.attrs["href"])})

    for school_link in school_links:
        print(school_link)

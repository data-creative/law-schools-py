import requests
from bs4 import BeautifulSoup
from IPython import embed

schools = []

def get_document(source="Remote"):
    document = None

    if source == "Remote":
        URL = "https://www.americanbar.org/groups/legal_education/resources/aba_approved_law_schools/official-guide-to-aba-approved-law-schools.html"
        print("REQUESTING REMOTE RESOURCE", URL)
        response = requests.get(URL)
        print("RESPONSE", response.status_code, response.encoding, dict(response.headers))
        document = response.text

    elif source == "Local":
        file_path = "mocks/official_school_guide.html"
        print("READING LOCAL FILE", file_path)
        with open(file_path, "r") as file:
            document = file.read()

    return document

doc = get_document(source="Local")

#soup = BeautifulSoup(doc, "lxml")
soup = BeautifulSoup(doc)

container = soup.find(id="main-tab-container") #.find("div") # the id of this div changes with each request, which is not helpful, so we find it from its parent div

embed()

for school in schools:
    print(school)

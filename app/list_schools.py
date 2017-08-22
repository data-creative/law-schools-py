import requests
from IPython import embed

schools = []

URL = "https://www.americanbar.org/groups/legal_education/resources/aba_approved_law_schools/official-guide-to-aba-approved-law-schools.html"
response = requests.get(URL)
print(type(response))
print(response.status_code)
print(response.text)

embed()

for school in schools:
    print(school)

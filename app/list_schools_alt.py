import csv
import json
from IPython import embed
from selenium import webdriver

URL = "http://employmentsummary.abaquestionnaire.org/"
driver = webdriver.Firefox()
driver.get(URL)

school_selector = driver.find_element_by_id("ddlUniversity")

school_options = school_selector.find_elements_by_tag_name("option") #> 207
school_options = [opt for opt in school_options if opt.text != "Select School"] #> 206

schools = []

for opt in school_options:
    school = {"name": opt.text, "uuid": opt.get_attribute("value")}
    print(school)
    schools.append(school)

driver.close() # important, closes browser

with open("data/schools_alt.csv", "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "uuid"])
    writer.writeheader()

    for school in schools:
        print(school)
        writer.writerow(school)

with open("data/schools_alt.json", "w") as json_file:
    json_file.write(json.dumps(schools))

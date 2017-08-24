#import requests
#from bs4 import BeautifulSoup
#import csv
#import re
#import json
from IPython import embed
from selenium import webdriver


URL = "http://employmentsummary.abaquestionnaire.org/"
driver = webdriver.Firefox()
driver.get(URL)

#
# SELECT SCHOOL
#

school_selector = driver.find_element_by_id("ddlUniversity")
school_options = school_selector.find_elements_by_tag_name("option") #> 207
school_options = [opt for opt in school_options if opt.text != "Select School"] #> 206
#for opt in school_options:
#    school = {"name": opt.text, "uuid": opt.get_attribute("value")}
#    print(school)
school_opt = school_options[-1] #> "YALE"
school_opt.click()

#
# SELECT YEAR
#

year_selector = driver.find_element_by_id("ddlYear")
year_options = year_selector.find_elements_by_tag_name("option")
year_opt = year_options[0] #> 2016
year_opt.click()

###form = page.forms.first
###button = page.form.button_with(:value => "Generate Report")
###response = agent.submit(form, button)

submission_button = driver.find_element_by_id("btnSubmit")

embed()


driver.close() # important, closes browser

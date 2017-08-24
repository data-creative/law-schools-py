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

school_selector = driver.find_element_by_id("ddlUniversity")

school_options = school_selector.find_elements_by_tag_name("option") #> 207

schools = []

for opt in school_options:
    school = {"name": opt.text, "uuid": opt.get_attribute("value")}
    print(school)
    schools.append(school)
    #opt.click()

#year_selector = driver.find_element_by_id("ddlYear")
###year_option = year_selector.options.find{|option| option.text == year.to_s}
###year_option.select

###form = page.forms.first
###button = page.form.button_with(:value => "Generate Report")
###response = agent.submit(form, button)





driver.close() # important, closes browser

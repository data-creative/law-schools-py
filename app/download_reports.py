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



embed()

#tables = driver.find_elements_by_tag_name("table")
#table = [table for table in tables if ("AKRON (1961)" in table.text and "YALE (1923)" in table.text)][0]
#table_html = table.get_attribute('innerHTML')



driver.close() # important, closes browser

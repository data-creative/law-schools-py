from IPython import embed
from selenium import webdriver
import os
import time
import shutil

REPORTS_DIR = os.getcwd() + "/reports"

def initialize_web_driver(download_dir=REPORTS_DIR):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2) # 0=Desktop, 1=Downloads, 2=custom
    profile.set_preference('browser.download.dir', download_dir)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") # this setting is required!
    profile.set_preference("pdfjs.disabled", True) # this setting is required!
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver

# @param option_elements A list full of items like: <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="42a9354b-6327-3b4a-9b5d-e6a84aaccce0", element="5d149448-0d88-cc45-a5fa-efbd7e8ab90f")>
def select_years(option_elements):
    available_years = [opt.text for opt in option_elements] #> ['2016', '2015', '2014', '2013', '2012', '2011', '2010']
    selection = input("Found the following available years: {0}. \n Please input the year you'd like to download, or input 'ALL' to download reports for all available years: ".format(available_years))

    if selection == "ALL":
        selected_year_opts = option_elements
    elif selection in available_years:
        selected_year_opts = [opt for opt in option_elements if opt.text == selection]
    else:
        print("UNRECOGNIZED YEAR SELECTION:", selection)
        selected_year_opts = [] # produces a no-op (iterating through empty list)
    return selected_year_opts

driver = initialize_web_driver()
driver.get("http://employmentsummary.abaquestionnaire.org/")

#submission_button = driver.find_element_by_id("btnSubmit")

year_selector = driver.find_element_by_id("ddlYear")
year_options = year_selector.find_elements_by_tag_name("option")
selected_year_options = select_years(year_options)
for year_opt in selected_year_options:
    print("SELECTING YEAR:", year_opt.text)
    year_opt.click()
    time.sleep(2)

    # note: school options change for different years, for example a school won't be included in the 2010 list if it was founded in 2012 (La Verne, Mass.)
    school_selector = driver.find_element_by_id("ddlUniversity") # if this is defined before the year selection,
    school_options = school_selector.find_elements_by_tag_name("option")
    school_options = [opt for opt in school_options if opt.text != "Select School"]
    print("... FOUND", len(school_options), "SCHOOLS")
    for school_opt in school_options:
        school = {"name": school_opt.text, "uuid": school_opt.get_attribute("value")}

        print(school)

        #school_opt.click()
        #submission_button.click() # download the report
        #time.sleep(2) # note: the download doesn't happen without the pause. this means we have to respect async actions.
        #reports = [os.path.join(REPORTS_DIR, f) for f in os.listdir(REPORTS_DIR) if f != '.DS_Store'] # adapted from source: https://stackoverflow.com/a/34548219/670433
        #report_last_downloaded = max(reports, key = os.path.getmtime) # todo: test this!
        #shutil.move(report_last_downloaded, os.path.join(REPORTS_DIR, "{0}-{1}.pdf".format(school["uuid"], school["name"])) ) # renames the file from what would otherwise be something like "EmploymentSummary-2017(2).pdf"
        #time.sleep(1)

driver.close() # important, closes browser window

#from IPython import embed
from selenium import webdriver
import os
import time
import shutil

URL = "http://employmentsummary.abaquestionnaire.org/"
REPORTS_DIR = os.getcwd() + "/reports"

#
# INITIALIZE DRIVER
#

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # 0=Desktop, 1=Downloads, 2=custom
profile.set_preference('browser.download.dir', REPORTS_DIR)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") # this setting is required!
profile.set_preference("pdfjs.disabled", True) # this setting is required!
driver = webdriver.Firefox(firefox_profile=profile)

#
# VISIT REPORTS PAGE
#

driver.get(URL)

#
# LOCATE BUTTON
#

submission_button = driver.find_element_by_id("btnSubmit")

#
# GET YEAR SELECTION OPTIONS
#

year_selector = driver.find_element_by_id("ddlYear")
year_options = year_selector.find_elements_by_tag_name("option")

#
# SELECT YEAR
#

year_opt = year_options[0]
year_opt.click()

#
# GET SCHOOL SELECTION OPTIONS
#

school_selector = driver.find_element_by_id("ddlUniversity")
school_options = school_selector.find_elements_by_tag_name("option") #> 207
school_options = [opt for opt in school_options if opt.text != "Select School"] #> 206

for i, opt in enumerate(school_options):
    school = {"name": opt.text, "uuid": opt.get_attribute("value")}
    print(school)

    #
    # SELECT SCHOOL
    #

    opt.click()
    submission_button.click()
    time.sleep(2) # note: the download doesn't happen without the pause. this means we have to respect async actions.

    #
    # DOWNLOAD REPORT
    #

    reports = [os.path.join(REPORTS_DIR, f) for f in os.listdir(REPORTS_DIR) if f != '.DS_Store'] # adapted from source: https://stackoverflow.com/a/34548219/670433
    report_last_downloaded = max(reports, key = os.path.getmtime) # todo: test this!
    shutil.move(report_last_downloaded, os.path.join(REPORTS_DIR, "{0}-{1}.pdf".format(school["uuid"], school["name"])) ) # renames the file from what would otherwise be something like "EmploymentSummary-2017(2).pdf"
    time.sleep(1)

driver.close() # important, closes browser window

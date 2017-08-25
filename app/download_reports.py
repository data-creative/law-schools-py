#import csv
#import json
from IPython import embed
from selenium import webdriver
import os

URL = "http://employmentsummary.abaquestionnaire.org/"
REPORTS_DIR = os.getcwd() + "/reports"

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # 0=Desktop, 1=Downloads, 2=custom
profile.set_preference('browser.download.dir', REPORTS_DIR)


mime_types = "application/pdf, application/xpdf, application/octet-stream"
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types);
profile.set_preference("browser.download.manager.showWhenStarting",False);
profile.set_preference("browser.helperApps.neverAsk.openFile", mime_types);
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.useWindow", False);
profile.set_preference("browser.download.manager.focusWhenStarting", False);
profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
profile.set_preference("browser.download.manager.showAlertOnComplete", False);
profile.set_preference("browser.download.manager.closeWhenDone", True);
profile.set_preference("pdfjs.disabled", True);

# NONE OF THIS JUNK WORKS, UNFORTUNATELY:
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword,application/csv,text/csv,application/rtf,application/xml,text/xml,application/octet-stream,application/vnd.ms-excel,application/zip,text/txt,text/plain,application/pdf,application/x-pdf");
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "application/msword, application/csv, text/csv, image/png, image/jpeg, application/pdf, text/html, text/plain, application/octet-stream")
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.helperApps.alwaysAsk.force', False);
#profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/octet-stream')
#profile.set_preference('browser.download.manager.showAlertOnComplete', False);
#profile.set_preference('browser.download.manager.closeWhenDone', False);



driver = webdriver.Firefox(firefox_profile=profile)
driver.get(URL)

#
# SUBMISSION BUTTON
#

submission_button = driver.find_element_by_id("btnSubmit")

#
# YEAR SELECTOR
#

year_selector = driver.find_element_by_id("ddlYear")
year_options = year_selector.find_elements_by_tag_name("option")
year_opt = year_options[0] #> 2016
year_opt.click()

#
# SCHOOL SELECTOR
#

school_selector = driver.find_element_by_id("ddlUniversity")
school_options = school_selector.find_elements_by_tag_name("option") #> 207
school_options = [opt for opt in school_options if opt.text != "Select School"] #> 206

for i, opt in enumerate(school_options[0:5]):
    school = {"name": opt.text, "uuid": opt.get_attribute("value")}
    print(school)

    opt.click()

    submission_button.click()

    #if i == 0: embed()  # allows the user to interact with dialog to click both "always ", then subsequent downloads will happen automatically


### CAN ACCESS THE POPUP DIALOG, BUT CAN'T INTERACT WITH IT UNFORTUNATELY:
###print("CURRENT WINDOW:", driver.current_window_handle, "ALL WINDOWS:", driver.window_handles)
###driver.switch_to_window("11")

driver.close() # important, closes browser window

#!/usr/bin/env python3.5

import selenium
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By



usr_name = "jareddyreson"
password = "Serebii2017!##"

upload_document_url = "https://goprintmobile.fullerton.edu/cps/Login.jsp"
driver = webdriver.Firefox() # options=option
wait = ui.WebDriverWait(driver, 60)
driver.get(upload_document_url)

# getting passed the first landing page

driver.find_element_by_name("principal").send_keys(usr_name)
driver.find_element_by_name("credentials").send_keys(password)
driver.find_element_by_name("Submit").click()

# wait for us to reach the landing page
wait.until(lambda webpageloaded: ec.title_is("{}".format("PrinterOn Printing Service")))
selectable_list_of_printers = [ element for element in driver.find_elements_by_class_name("box.printerlink.sorting_1") ]
list_of_printers = [ printer.text for printer in selectable_list_of_printers ]
# printing the available pritners (for future use)
# for printer in list_of_printers:
#     print(printer)
# driver.find_element(By.PARTIAL_LINK_TEXT("SGC_wPLN1BlackWhite4 ")).click()
driver.find_element_by_partial_link_text("SGC_wPLN1BlackWhite4 ").click()
# for printer in selectable_list_of_printers:


# clean up
def clean_up():
    sleep(5)
    driver.close()
    os.remove("geckodriver.log")
# clean_up()

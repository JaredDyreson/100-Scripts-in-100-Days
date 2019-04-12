#!/usr/bin/env python3.5
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime

url = "https://www.wunderground.com/history"
option = Options()
option.headless = True
driver = webdriver.Firefox() # options=option
driver.get(url)
driver.find_element_by_id("histSearch").send_keys("90631")
# time_needed = datetime.datetime.strptime(sys.argv[1], "%")
driver.find_element_by_class_name("month").send_keys("4")
driver.find_element_by_class_name("day").send_keys("28")
driver.find_elements_by_class_name("year").send_keys("1999")

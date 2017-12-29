# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:51:08 2015

@author: Sang
"""

from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

f_sele=codecs.open('truedelta.txt',encoding='utf-8',mode='w')
url = 'http://www.truedelta.com/problems'


driver = webdriver.Firefox()

driver.get(url)
driver.implicitly_wait(10)

"""
report_element= driver.find_element_by_id('compare-report')
report_all_options = report_element.find_elements_by_tag_name("option")
report_count=0
for report_option in report_all_options:
    report_count += 1
    if (report_count==2):
        print("report value is: %s" % report_option.get_attribute("value"))
        report_option.click()
        break


year_element= driver.find_element_by_id('compare-year')
year_all_options = year_element.find_elements_by_tag_name("option")
year_count=0
for option in year_all_options:
    year_count += 1
    if (year_count==3):
        print("Value is: %s" % option.get_attribute("value"))
        option.click()
        break
#    option.click()


make_element= driver.find_element_by_id('compare-make')
make_all_options = make_element.find_elements_by_tag_name("option")
make_count=0
for make_option in make_all_options:
    make_count += 1
    if (make_count==2):
        print("make value is: %s" % make_option.get_attribute("value"))
        make_option.click()
        break

"""

select1 = Select(driver.find_element_by_name('year'))
select1.select_by_visible_text('2016')

select2 = Select(driver.find_element_by_name('brand'))
select2.select_by_visible_text('Acura')

select3 = Select(driver.find_element_by_name('model'))
select3.select_by_value('293')

select4 = Select(driver.find_element_by_name('problem_area'))
select4.select_by_visible_text('Engine')
"""
model_element= driver.find_element_by_id('compare-model')
model_all_options = model_element.find_elements_by_tag_name("option")
model_count=0
for option in model_all_options:
    model_count += 1
    if (model_count==2):
        print("Value is: %s" % option.get_attribute("value"))
        #option.click()
        break
"""
submit_element = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/form/fieldset/div/input[2]')
submit_element.click()

contents = ''

html = driver.page_source
no_result = re.compile('No Results')

if (not re.findall(no_result, html)):
    soup = BeautifulSoup(html)
    try :
        contents = soup.find(id="problems")
    except Exception:
        print ("error")
    print(contents)
else :
    print("empty page")


driver.close()

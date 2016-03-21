# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:10:10 2015

@author: Administrator
"""

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

truedelta_url = 'http://www.truedelta.com/problems'

## Select model Id : rh-model, xpath : /html/body/div[3]/div[2]/div/div[1]/form/fieldset/table/tbody/tr[4]/td/select 

driver = webdriver.Firefox()
driver.get(truedelta_url)
driver.implicitly_wait(10)

# get id
# element_year = driver.find_element_by_id('rh-model-year')
# element_make = driver.find_element_by_id('rh-make')
# element_model = driver.find_element_by_id('rh-model')

# get xpath
element_model = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/form/fieldset/table/tbody/tr[4]/td/select[@name='model']")

search = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/form/fieldset/div/input[2]")
no_result = re.compile('No Results')

# get list 
list_year = [x for x in element_year.find_elements_by_tag_name("option")]

# print("brand = "+str(list_brand))

# print("model = "+str(list_model))

for year in list_year:
    if (year.get_attribute("value") == "") :
        continue
    else :
        year.click()
        list_brand = [x for x in element_brand.find_elements_by_tag_name("option")]
        for brand in list_brand:
            # brand.text - option text 값
            # brand.get_attribute("value") - option value값            
            if (brand.get_attribute("value") == ""):
                continue
            else:
                brand.click()
                list_model = [x for x in element_model.find_elements_by_tag_name("option")]
                for model in list_model:
                    if (model.get_attribute("value") == ""):
                        continue
                    else:                        
                        model.click()
                        list_probarea = [x for x in element_probarea.find_elements_by_tag_name("option")]
                        for prob in list_probarea:
                            if (prob.get_attribute("value")== ""):
                                continue
                            else:
                                prob.click()
                                search.click()
                                html = driver.page_source
                                print(html)
                                ## No Results 여부 판단
                                if (not re.findall(no_result, html)):
                                    print("1")
                                    soup = BeautifulSoup(html)
                                    try :
                                        print("2")
                                        # 수리내역 가져오기
                                        contents = soup.find(id="problems")
                                        print(contents)
                                    except Exception:
                                        continue
                                else:
                                    continue
                            print("!!!")          
                            driver.back()
                            continue
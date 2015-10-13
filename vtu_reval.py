#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from util import mail
import time,re,unicodedata
from selenium.webdriver.common.keys import Keys

def vtu(name,email):	
	driver = webdriver.PhantomJS()
	#Presently the code is used to get revaluation results
	#Change the vitavireval to vitavi in the below statement for normal results
	driver.get("http://results.vtu.ac.in/vitavireval.php")
	sbox=driver.find_element_by_xpath('//input[contains(@type, "TEXT")]')
	sbox.send_keys(name)
	sbox.send_keys(Keys.RETURN)
	has=str((BeautifulSoup(driver.page_source)).find('td' ,{ 'width' : '513'}))
	ker=re.sub("\n","", ((((BeautifulSoup(driver.page_source)).find('td' ,{ 'width' : '513'})).text)))
	if(ker != "Results are not yet available for this university seat number  or it might not be a  valid university seat numberClick here to go back"):
	    return mail(email,has,"VTU revaluation results",time.strftime("%d/%m/%Y"),1)
	driver.quit()


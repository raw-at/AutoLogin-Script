#Facebook Script

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import commands



#path to chrome driver saved 
path_to_chrome = '/home/brutal/Desktop/chromedriver'


#Driver for website Chrome Instance
driver = webdriver.Chrome(executable_path = path_to_chrome)

#facebook url
driver.get('https://www.facebook.com/')



search_tab = driver.find_element_by_xpath('//*[@id="email"]')
search_tab.send_keys('#enter email here')



password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('#enter password here')


log_in = driver.find_element_by_xpath('//*[@id="loginbutton"]')
log_in.click()


import os
from selenium import webdriver
import time

#open the webpage
driver = webdriver.Chrome()
driver.get('https://www.1point3acres.com/bbs')

#fill in username and password respectively
id_box = driver.find_element_by_id('ls_username')
id_box.send_keys('airstrikers')

pwd_box = driver.find_element_by_id('ls_password')
pwd_box.send_keys('4ffZp69oY*mP')

#login
login_button = driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/table/tbody/tr/td/button")
login_button.click()

#sign in
signin_link = driver.find_element_by_link_text("签到领奖!")
signin_link.click()

#wait for certain time
time.sleep(4)
icon_button = driver.find_element_by_xpath("/html/body/div/div/table/tbody/tr/td/form/div/table/tbody/tr/td/ul/li")
#print(icon_button.get_attribute("onclick"))
#print(icon_button.get_attribute("id"))
icon_button.click()

todaySay_box = driver.find_element_by_id("todaysay")
todaySay_box.send_keys('今天感觉很开心')

sigin_button = driver.find_element_by_xpath("/html/body/div/div/table/tbody/tr/td/form/p/button")
sigin_button.click()

driver.close()

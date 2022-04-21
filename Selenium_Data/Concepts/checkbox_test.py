from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://automationpractice.com/index.php')
driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a').click() #Finds a element by using xpath

tickbox = driver.find_element_by_css_selector("input[name=layered_category_8]") #Finds a checkbox using \
        #css_selector bcoz all checkboxes having same type='checkbox'

driver.find_element_by_css_selector("input[name=layered_category_8]").click()

print(tickbox.is_selected()


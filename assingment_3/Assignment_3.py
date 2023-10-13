from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

#Navigating to the FudDelivery app
driver.get("https://www.linkedin.com")
time.sleep(3)

#Click on Username
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
linkedin_uname= driver.find_element(By.ID,"session_key")
linkedin_uname.send_keys("kadamprashantarun@gmail.com")
time.sleep(3)

#Click on Password
linkedin_password= driver.find_element(By.ID, "session_password")
linkedin_password.send_keys("shivaji123*")
time.sleep(3)

#Click on SignIn button
signin_button = driver.find_element(By.XPATH,"//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
signin_button.click()
time.sleep(3)


#Assert title
try:
    title = driver.title
    assert '(2) Feed | LinkedIn' in title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed', format(e))



#Search field enter search item
search_field = driver.find_element(By.XPATH,"//*[@id='global-nav-typeahead']/input")
search_field.send_keys("Senior Consultant")
time.sleep(2)
search_field.send_keys(Keys.ENTER)
time.sleep(3)



#Click on Home tab
home_tab = driver.find_element(By.XPATH,"//*[@id='global-nav']/div/nav/ul/li[1]/a/div")
home_tab.click()
time.sleep(3)



driver.quit()








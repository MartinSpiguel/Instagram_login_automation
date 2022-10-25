from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

my_username = 'example1'
my_password = '1234567'

driver = webdriver.Edge() 
driver.get('https://www.instagram.com')
assert 'Instagram' in driver.title

driver.maximize_window()
driver.implicitly_wait(5)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.clear()
password.clear()

username.send_keys(my_username)
password.send_keys(my_password)

username.send_keys(Keys.RETURN)
password.send_keys((Keys.RETURN))

time.sleep(5)

driver.close()

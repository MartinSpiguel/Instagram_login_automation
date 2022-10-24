from selenium import webdriver

driver = webdriver.Chrome() #Error: https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
                            #It´s also in Selenium docs (Installation--->Drivers)
driver.get('https://chess.com')
assert 'Chess' in driver.title
print(driver)
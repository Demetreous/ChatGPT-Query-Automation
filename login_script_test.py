# Libraries for automization
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


# Initializes web driver for Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(10) # This lets webdriver wait 10 seconds for the website to load
driver.get("https://chat.openai.com") # ChatGPT website

# Wait
driver.implicitly_wait(5)
#Find button by xpath
login_button = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div[4]/button[1]')
#Click button
driver.execute_script('arguments[0].click();', login_button)


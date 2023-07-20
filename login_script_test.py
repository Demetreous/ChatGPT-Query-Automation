# Authors: Demetreous Stillman, Zergio

# Libraries for automization
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox() # Initializes web driver for Firefox
driver.implicitly_wait(10) # This lets webdriver wait 10 seconds for the website to load
driver.get("https://chat.openai.com") # ChatGPT website


driver.implicitly_wait(10) # Wait
login_button = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div[4]/button[1]') #Find button by xpath
driver.execute_script('arguments[0].click();', login_button) #Click button


'''
Email and password for testing:
    Email: gptquerytesting@gmail.com
    Password: #gptquerytesting19
'''


# Enters the username
driver.implicitly_wait(5)
email_textbox = driver.find_element('xpath', '//*[@id="username"]')
email_textbox.send_keys("gptquerytesting@gmail.com")

# Presses the continue button
continue_button = driver.find_element('xpath', '/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button') #Find button by xpath
driver.execute_script('arguments[0].click();', continue_button) #Click button

# Enters the password
driver.implicitly_wait(3) # Wait
password_textbox = driver.find_element('xpath', '//*[@id="password"]')
password_textbox.send_keys("#gptquerytesting19")

# Presses the continue button
continue_button = driver.find_element('xpath', '/html/body/div/main/section/div/div/div/form/div[3]/button') #Find button by xpath
driver.execute_script('arguments[0].click();', continue_button) #Click button

'''
Problem:
After logging in openAI scans your browser to see if it's a bot.
The browser failed this test and google then disabled the test account
'''

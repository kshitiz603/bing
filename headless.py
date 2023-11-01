from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import ast
from txt import txt

# Create a WebDriver instance
driver = webdriver.Edge()


driver.get("https://bing.com/search?q=hlo")

# Load the stored cookies
for x in range(28,29):
    with open('cookies/' + str(x)+ '.txt', 'r') as cookies_file:
        cookies = ast.literal_eval(cookies_file.read())

    time.sleep(1.15)

# Add the stored cookies to the current session
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(1.15)


#search start
    driver.get("https://bing.com/search?q=hlo")

    for i in range(0,1):
        time.sleep(0.15)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()

        time.sleep(1)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(random.choice(txt))
        
        time.sleep(0.6)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(Keys.RETURN)
        
        time.sleep(0.2)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()

 
#loop unit enter
input("Press Enter to quit...")
# Close the WebDriver when you're done
driver.quit()

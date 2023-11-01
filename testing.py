from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import ast
import random
from txt import txt

# Create a WebDriver instance
driver = webdriver.Edge()

#wait for some time
driver.implicitly_wait(8)


#login start

# Navigate to a webpage 

#driver.get("https://rewards.bing.com/")


#search start
driver.get("https://bing.com/search?q=hlo")


time.sleep(2)
# Load the stored cookies

with open('cookies/28.txt', 'r') as cookies_file:
    cookies = ast.literal_eval(cookies_file.read())

time.sleep(1)

# Add the stored cookies to the current session
for cookie in cookies:
    driver.add_cookie(cookie)



input("Press Enter after login...")

"""

for i in range(0,32):
    time.sleep(0.25)
    driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()

    time.sleep(4)
    driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(random.choice(txt))
        
    time.sleep(0.25)
    driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(Keys.RETURN)

    time.sleep(0.25)
    driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()
"""

#time.sleep(60)


time.sleep(1)

# Store the cookies in a file
with open('cookies/cookies.txt', 'w') as cookies_file:
    cookies_file.write(str(driver.get_cookies()))



#loop unit enter
input("Press Enter to quit...")

time.sleep(0.1)
#clear cookies
driver.delete_all_cookies()


# Close the WebDriver when you're done
driver.quit()
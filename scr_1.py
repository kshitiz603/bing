from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import ast
from txt import txt




# creating csv file
filename = "points.csv"

# open csv file to write
f = open(filename, 'a', newline=' ')


# Create a WebDriver instance
driver = webdriver.Edge()



driver.get("https://bing.com/search?q=hlo")

# Load the stored cookies
for x in range(1,8):
    with open('cookies/' + str(x)+ '.txt', 'r') as cookies_file:
        cookies = ast.literal_eval(cookies_file.read())

    time.sleep(1.15)

# Add the stored cookies to the current session
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(1.15)


#search start
    driver.get("https://bing.com/search?q=hlo")

    for i in range(0,35):
        time.sleep(0.25)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()

        time.sleep(1)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(random.choice(txt))
        
        time.sleep(0.6)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").send_keys(Keys.RETURN)
        
        time.sleep(0.25)
        driver.find_element(By.XPATH,
                        "/html/body/header/form/div/textarea").clear()

#write in csv
    driver.refresh()
    time.sleep(2)

    acc = driver.find_element(By.XPATH,
                              "/html/body/header/div/a[1]/span[2]").text
    points = driver.find_element(By.XPATH,
                                 "/html/body/header/div/a[2]/span[1]").text
    
    f.write(str(acc) + " " + str(points) + "\n")

#clear cookies
    #input("enter to delete cookies")
    driver.delete_all_cookies()
    time.sleep(1)
    
#loop unit enter
input("Press Enter to quit...")
# Close the WebDriver when you're done
driver.quit()
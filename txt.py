"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import ast
import random



# Create a WebDriver instance
driver = webdriver.Edge()

#wait for some time
driver.implicitly_wait(8)


# Define your desired mobile device characteristics
mobile_emulation = {
    "deviceName": "iPhone X"  # You can change this to another device profile
}


# Configure Edge WebDriver with mobile emulation settings
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Create the WebDriver instance with the EdgeOptions
driver = webdriver.Edge(options=edge_options)

# Navigate to a website
#search start
driver.get("https://bing.com/search?q=hlo")


time.sleep(2)
# Load the stored cookies

with open('anshu_cook.txt', 'r') as cookies_file:
    cookies = ast.literal_eval(cookies_file.read())

time.sleep(1)

# Add the stored cookies to the current session
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(1)

#loop unit enter
input("Press Enter to quit...")



# Perform your testing or interactions with the website in mobile view

# Don't forget to close the driver when you're done
driver.quit()
"""


txt = [
    "How to bake a chocolate cake?",
    "Best travel destinations in 2023",
    "What is climate change?",
    "How to improve productivity at work?",
    "Symptoms of the common cold",
    "Healthy breakfast recipes",
    "Famous quotes by Albert Einstein",
    "How to learn a new language quickly?",
    "How does photosynthesis work?",
    "Top action movies of all time",
    "How to meditate for beginners?",
    "How to fix a leaky faucet?",
    "What is the stock market?",
    "How to create a budget spreadsheet?",
    "Tips for weight loss and fitness",
    "How to grow tomatoes in a garden?",
    "Interesting facts about space exploration",
    "How to write a cover letter for a job application?",
    "Best books to read in 2023",
    "How to take care of indoor plants?"
]



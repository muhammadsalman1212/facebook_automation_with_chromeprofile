import time

from selenium import webdriver

# Path to the Chrome profile directory
profile_directory = r"C:\Users\user\Documents\all_profiles\Profile 2"

# Instantiate ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Add the user-data-dir option to specify the profile directory
chrome_options.add_argument(fr'user-data-dir={profile_directory}')

# Launch Chrome WebDriver with the specified profile
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://facebook.com/")
driver.get("https://www.facebook.com/groups/1046367672721054/members/")
time.sleep(5)
scrolls = 10  # Kitni baar scroll karna hai, aap isko apne requirement ke hisaab se adjust kar sakte hain

for i in range(scrolls):
    # Scroll karne ke liye JavaScript code ka upyog karein
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# i want to get driver html code





time.sleep(5555)



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize Selenium WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.facebook.com/")
driver.maximize_window()

email_input = driver.find_element(By.XPATH, '//input[@aria-label="Email address or phone number"]')
email_input.send_keys("ameershadev786@gmail.com")

password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys("Ameeralishah12")
password_input.send_keys(Keys.ENTER)

time.sleep(9)
click_on_groups = driver.find_element(By.XPATH, '//span[text()="Groups"]')
click_on_groups.click()
time.sleep(5)

search_groups = driver.find_element(By.XPATH, '//input[@aria-label="Search groups"]')
search_groups.send_keys("Python clients")
search_groups.send_keys(Keys.ENTER)
time.sleep(5)

click_on_join_groups = driver.find_elements(By.XPATH, "//span[text()='Join']")
for all_groups in click_on_join_groups:
    all_groups.click()
    time.sleep(5)



time.sleep(7)











time.sleep(2500000)
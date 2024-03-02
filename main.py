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

profile_btn = driver.find_element(By.XPATH, '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h"]//span')
profile_btn.click()

time.sleep(25)
for i in range(10):
    time.sleep(22)
    photo_video_btn = driver.find_element(By.XPATH, '//span[text()="Photo/video"]')
    photo_video_btn.click()
    time.sleep(15)
    # add_photo_video_btn = driver.find_element(By.XPATH, '//div[@class="x14yjl9h xudhj91 x18nykt9 xww2gxu x6s0dn4 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x3nfvp2 xl56j7k x1n2onr6 x1qhmfi1 x1vqgdyp x100vrsf"]//i')
    # add_photo_video_btn.click()



    photo_upload_input = driver.find_element(By.XPATH, '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
    photo_upload_input.send_keys(r"C:\Users\user\PycharmProjects\facebook_automation\chrome_dyVN8O2M32.png")
    time.sleep(7)
    photo_text = driver.find_element(By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
    photo_text.send_keys("Hello World")
    time.sleep(7)

    one_more_photo = driver.find_element(By.XPATH, '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
    one_more_photo.send_keys(r"C:\Users\user\PycharmProjects\facebook_automation\chrome_dyVN8O2M32.png")

    time.sleep(7)

    post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
    post_button.click()
    time.sleep(8)


time.sleep(33333)







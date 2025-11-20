from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# -------------------------
# ChromeDriver Setup
# -------------------------
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# IMPORTANT: Path to your ChromeDriver
service = Service("C:/chromedriver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

print("Opened Chrome")

# -------------------------
# Open YouTube
# -------------------------
driver.get("https://www.youtube.com")
print("Opened YouTube")
time.sleep(3)

# -------------------------
# Search for video
# -------------------------
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("L1. Introduction to LinkedList | Traversal | Length | Search an Element")
search_box.send_keys(Keys.RETURN)
print("Searched for video")
time.sleep(3)

# -------------------------
# Click the first video
# -------------------------
video = driver.find_element(By.XPATH, "//a[@id='video-title']")
video_title = video.text.strip()
video.click()
print("Opened video:", video_title)
time.sleep(5)

# -------------------------
# Activate video player
# -------------------------
video_player = driver.find_element(By.CSS_SELECTOR, "video")
video_player.click()
print("Activated video player")
time.sleep(1)

body = driver.find_element(By.TAG_NAME, "body")

# -------------------------
# Keyboard Controls
# -------------------------
body.send_keys("k")   # Play/Pause
print("Pressed K - Play/Pause")
time.sleep(2)

body.send_keys("f")   # Fullscreen
print("Pressed F - Fullscreen")
time.sleep(2)

body.send_keys("m")   # Mute
print("Pressed M - Mute")
time.sleep(2)

body.send_keys(Keys.ARROW_RIGHT)  # Forward 5s
print("Pressed → - Forward")
time.sleep(2)

body.send_keys(Keys.ARROW_LEFT)   # Backward 5s
print("Pressed ← - Backward")
time.sleep(3)

print("Automation Completed Successfully")

time.sleep(5)
driver.quit()

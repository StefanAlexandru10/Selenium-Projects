import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
txt = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
splitText = txt.split(" ")
emailText = ""
for word in splitText:
    if "@" in word:
        emailText = word + emailText
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(emailText)
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
message = driver.find_element(By.XPATH, "//form[@id='login-form']//strong/..")
wait.until(expected_conditions.visibility_of(message))
print(message.text)

time.sleep(55)

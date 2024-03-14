import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
top_link = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Reload"))
)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).click().perform()


time.sleep(55)

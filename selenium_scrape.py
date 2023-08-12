import time

PROMPT = "Hi"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://chat.vercel.ai/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "textarea"))
)
# text_area = driver.find_elements(By.TAG_NAME, "textarea")
# text_area[0].clear()
# text_area[0].send_keys(PROMPT)
# text_area[0].send_keys(Keys.RETURN)
# # WebDriverWait(driver, 10).until(
# #     EC.presence_of_element_located((By.XPATH, '//*[@title="OpenAI icon"]'))
# # )
# print("Response generated")
time.sleep(10)
output = driver.find_elements(By.TAG_NAME, "p")
print([op.text for op in output])
print(driver.title)

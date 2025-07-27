from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome(service=service)
driver.get("https://playful-torrone-162c28.netlify.app")
sleep(2)

login_button = driver.find_element(By.XPATH, '//span[tect()="Login]')
login_button.click()

# Preenche os campos de login
driver.find_element(By.NAME, 
                    "email").send_keys("qualityassurance@bertoni.com.br")
driver.find_element(By.NAME, "password").send_keys("versar123")

#Efetua o login e entra na página
driver.find_element(By.TAG_NAME, "form").submit()

sleep(10)
#driver.quit()
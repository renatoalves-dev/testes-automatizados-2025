from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o GGAS
driver.get("https://google.com")

# elements = driver.find_element(By.LINK_TEXT, "Imagens")

# busca = driver.find_element(By.ID, "APjFqb")

# busca.send_keys("computador")

# busca.click()


links = driver.find_element(By.LINK_TEXT, 'Imagens')
for link in links:
    link.click()


time.sleep(10)
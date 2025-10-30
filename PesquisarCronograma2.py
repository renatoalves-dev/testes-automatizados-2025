from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import TimeoutException
import time

import selenium.webdriver.common.keys

from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.FirefoxOptions()


# carregando uma página da Internet via Firefox
driver = webdriver.Firefox(options=options)

# Acessando o URL da GGAS

driver.get("https://ggas.copergas.com.br/ggas-teste-qintess")




title = driver.title
print(title)

# Encontrando a caixa de Login e realizando uma ação

login = driver.find_element(By.ID, "login").send_keys("caroline")
senha = driver.find_element(By.ID, "senha").send_keys("Admin123")
button = driver.find_element(By.ID, "button3").click()

driver.fullscreen_window()
time.sleep(10)
buscaFaturamento = driver.find_element(By.ID, "inputPesquisar").send_keys("Faturamento")
busca = driver.find_element(By.XPATH, '//*[@id="71"]/a/span')
busca.click()

grupoFaturamento = driver.find_element(By.NAME, "grupoFaturamento")
selectUnidade = Select(grupoFaturamento)
selectUnidade.select_by_value('886')
botaoPesquisar = driver.find_element(By.ID, "botaoPesquisar").click()
time.sleep(20)

proximo = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/form/div/div[2]/div[4]/div/div[3]/div[2]/div/ul/li[9]/a').click()
selecionar = driver.find_element(By.XPATH, '//*[@id="cronograma"]/tbody/tr[7]/td[7]/a').click()
time.sleep(10)




# webElement = driver.find_element(By.CSS_SELECTOR, "#atividade > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1)")
# webElement.sendKeys(Keys.TAB);
# time.sleep(20)
# href = driver.find_element((By.CSS_SELECTOR, "#atividade > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)")).click()


#href = driver.find_element((By.XPATH, '//*[@id="atividade"]/tbody/tr[1]/td[1]/a'))
# href.click()

time.sleep(10)
i = 1
while i <= 10:
    footer = driver.find_element(By.ID, "buttonAlterar")
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    print('It has scrolled ' + str(i) + ' times')
    print('Now waiting 3 seconds before repeating')
    time.sleep(3)
    i += 1

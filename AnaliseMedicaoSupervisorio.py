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
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import selenium.webdriver.common.keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import js2py
import pytest
import pytest_html
options = webdriver.FirefoxOptions()



# carregando uma página da Internet via Firefox
driver = webdriver.Firefox(options=options)
options.set_preference("general.smoothScroll", True)
# Acessando o URL da GGAS
driver.get("https://ggas.copergas.com.br/ggas-teste-qintess")




title = driver.title
print(title)



    
# Encontrando a caixa de Login e realizando uma ação
 
try:
    
 login = driver.find_element(By.ID, "login").send_keys("caroline")
 senha = driver.find_element(By.ID, "senha").send_keys("Admin123")
 button = driver.find_element(By.ID, "button3").click()
 
except Exception as e:
    print(e)
    
driver.fullscreen_window()
time.sleep(10)
buscaFaturamento = driver.find_element(By.ID, "inputPesquisar").send_keys("Medição")

analiseMedicao = driver.find_element(By.XPATH, '//*[@id="305"]/a/span').click()

time.sleep(10)

################################ COMEÇANDO A SELECIONAR CAMPOS NO FORMULÁRIO ##############################

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "anormalidade")))
grupoFaturamento = driver.find_element(By.ID, "grupoFaturamento")
selectOption = Select(grupoFaturamento)
selectOption.select_by_value('1086')

time.sleep(20)




# selectOption4 = Select(anormalidade1)
# selectOption4.select_by_value("33")
# time.sleep(5)

# pontoConsumo = driver.find_element(By.XPATH, '//*[@id="formPesquisaAnaliseMedicaoSupervisorio"]/div/div[2]/div[2]/div/div[2]/div[1]/span/span[1]/span/ul/li/input')
# pontoConsumo.click()

# modal = driver.find_element(By.ID, "descricaoPontoConsumo_modal").send_keys("123")

time.sleep(10)


# time.sleep(10)
# buttonModal = driver.find_element(By.ID, "btnEscolherPontosConsumo").click()
segmento = driver.find_element(By.ID, "segmento")
selectOption1 = Select(segmento)
selectOption1.select_by_value('2')

comAnormalidade = driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(5) > div:nth-child(1) > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(2)")
comAnormalidade.click()


anormalidade1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div[2]/div[2]/div/div[4]/div[1]/fieldset/span/span[1]/span/ul/li[1]").click()
# dropdown = Select(driver.find_element(By.ID,"anormalidade"))
# for opt in dropdown.options:
#     dropdown.select_by_visible_text(opt.get_attribute("innerText")) 
# dropdown.select_by_visible_text('REGISTRO DUPLICADO')
# referencia = driver.find_element(By.ID, "referencia")
# options.set_preference('javascript.enabled', False)
# time.sleep(5)
# referencia.click()
# referencia.send_keys("01/2023")

options.set_preference('javascript.enabled', True)



buttonPesquisar = driver.find_element(By.ID, "botaoPesquisar").click()



time.sleep(10)


################# while ######################## SCROOL TO THE FOOTER OF PAGE ###############################################

i = 1
while i <= 10:
    footer = driver.find_element(By.ID, "btnExportar")
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    print('It has scrolled ' + str(i) + ' times')
    print('Now waiting 3 seconds before repeating')
    time.sleep(3)
    i += 1
    
    c = 1
else:
    while c <= 10:
      footer1 = driver.find_element(By.ID, "tabelaAnaliseMedicaoSupervisorio")
      driver.execute_script("arguments[0].scrollIntoView();", footer1)
      print('It has scrolled ' + str(c) + ' times')
      print('Now waiting 3 seconds before repeating')
      time.sleep(3)
      c += 1

scheight = .1
while scheight < 35.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
    
    
    
time.sleep(10)    


driver.save_full_page_screenshot("screenShoot_2024.png")
    


#expandir = driver.find_element(By.XPATH, '//*[@id="expandir"]')


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
import selenium.webdriver.common.keys
import requests
from bs4 import BeautifulSoup
import pdb
import requests


options = webdriver.FirefoxOptions()


# carregando uma página da Internet via Firefox
driver = webdriver.Firefox(options=options)

# Acessando o URL da GGAS

url = "https://ggas.copergas.com.br/ggas-teste-qintess"
driver.get(url)




title = driver.title
print(title)

# Encontrando a caixa de Login e realizando uma ação

login = driver.find_element(By.ID, "login").send_keys("carol")
senha = driver.find_element(By.ID, "senha").send_keys("Admin123")
button = driver.find_element(By.ID, "button3").click()


driver.fullscreen_window()
time.sleep(10)
buscaFaturamento = driver.find_element(By.ID, "inputPesquisar").send_keys("Faturamento")
busca = driver.find_element(By.XPATH, '//*[@id="71"]/a/span')
busca.click()

time.sleep(10)

grupoFaturamento = driver.find_element(By.NAME, "grupoFaturamento")
selectUnidade = Select(grupoFaturamento)
selectUnidade.select_by_value('1726')

periodicidade = driver.find_element(By.NAME, "periodicidade")
selectUnidade = Select(periodicidade)
selectUnidade.select_by_value('4')

status = driver.find_element(By.ID, "situacao")
selectUnidade = Select(status)
selectUnidade.select_by_value("Em Andamento")

# ultimaEtapa = driver.find_element(By.ID, "ultimaEtapa")
# selectUnidade = Select(ultimaEtapa)
# selectUnidade.select_by_value('1')
########## DATA INICIAL
mesAnoFaturamentoInicial = driver.find_element(By.XPATH, '//*[@id="mesAnoFaturamentoInicial"]')
options.set_preference('javascript.enabled', False)
time.sleep(5)
mesAnoFaturamentoInicial.click()
mesAnoFaturamentoInicial.send_keys("11/2024")


time.sleep(10)


####### DATA FINAL
mesAnoFaturamentoFinal = driver.find_element(By.ID, "mesAnoFaturamentoFinal")
options.set_preference('javascript.enabled', False)
time.sleep(5)
mesAnoFaturamentoFinal.click()
mesAnoFaturamentoFinal.send_keys("11/2024")

options.set_preference('javascript.enabled', True)
botaoPesquisar = driver.find_element(By.ID, "botaoPesquisar").click()


time.sleep(10)
############################//*[@id="checkboxChavesPrimarias5333"]#############################
#checkBox = driver.find_element(By.XPATH, '//*[@id="checkboxChavesPrimarias5333"]').click()

time.sleep(10)
###################### DETALHAR CRONOGRAMA
detalharCronograma = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div[2]/div[4]/div/div[2]/div/table/tbody/tr/td[3]/a").click()
time.sleep(30)

print(detalharCronograma)
# # Coleta dados de um link <a href
# rows = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div[2]/div[4]/div/div[2]/div/table/tbody/tr/td[3]/a")
# for row in rows:
#     print(row.text)


############### CONSOLIDAR ENGRENAGEM API CONSOLIDAR DADOS SUPERVISÓRIO as vezes fora
consolidarDadosEngrenagem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/a").click()
pdb.set_trace()
driver.save_screenshot('consolidar1.png')
time.sleep(10)

############### OPTION SELECIONAR  
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div/div[2]/div[2]/div/div[15]/select/option").click()

######## BUTTON EXECUTAR CONSOLIDAR DADOS
button = driver.find_element(By.XPATH, '//*[@id="botaoExecutar"]').click()

time.sleep(20)

######### LOOP PARA FOOTER
i = 1
while i <= 5:
    footer = driver.find_element(By.ID, "tableProcessos_info")
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    print('It has scrolled ' + str(i) + ' times')
    print('Now waiting 3 seconds before repeating')
    time.sleep(5)
    i = i + 1
    

########################## LOOP PARA HEADER ##########################

c = 1
while c <= 10:

  header = driver.find_element(By.CLASS_NAME,"card-header")
  driver.execute_script("arguments[0].scrollIntoView();", header)
  print('It has scrolled ' + str(c) + ' times')
  print('Now waiting 3 seconds before repeating')
  time.sleep(2)
  c = c + 1
 
 ########### SCROLL SMOOTHLY 
 
scheight = .1
while scheight < 43.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.4);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.5);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.7);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.8);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.3);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.5);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.7);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.9);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5.2);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5.1);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5.8);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.7);")
# time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/50);")
# time.sleep(10) 
       
# ALTERNATIVA AO ID
#driver.execute_script('document.getElementById("submitMe").click()')

#idGrupoFaturamento

grupoFaturamento = driver.find_element(By.ID, "idGrupoFaturamento")
selectGrupoFaturamento = Select(grupoFaturamento)
selectGrupoFaturamento.select_by_value('1726')

pesquisarResultadoFinal = driver.find_element(By.ID, "botaoPesquisar").click()

time.sleep(10)

######### LOOP PARA FOOTER
i = 1
while i <= 5:
    
    footer = driver.find_element(By.ID, "tableProcessos_info")
    #footer = driver.execute_script('document.getElementById("tableProcessos_info")')
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    print('It has scrolled ' + str(i) + ' times')
    print('Now waiting 3 seconds before repeating')
    time.sleep(5)
    i = i + 1
    

############################### SCROLL SMOOTHLY 
 
scheight = .1
while scheight < 43.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
    
driver.save_full_page_screenshot('consolidarSucesso.png')   

time.sleep(20) 

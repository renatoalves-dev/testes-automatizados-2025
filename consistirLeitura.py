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
from webdriver_manager.chrome import ChromeDriverManager  

options = webdriver.FirefoxOptions()


# carregando uma página da Internet via Firefox
driver = webdriver.Firefox(options=options)
#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)
# Acessando o URL da GGAS

url = "https://ggas.copergas.com.br/ggas-teste-qintess/"
driver.get(url)




title = driver.title
print(title)

# Encontrando a caixa de Login e realizando uma ação

login = driver.find_element(By.ID, "login").send_keys("carol.qintess")
senha = driver.find_element(By.ID, "senha").send_keys("Admin123")
button = driver.find_element(By.ID, "button3").click()


driver.fullscreen_window()
time.sleep(10)

#####################  CONSISTIR LEITURA ##############################

#buscaConsistirLeitura = driver.find_element(By.ID, "inputPesquisar").send_keys("Medição")
time.sleep(3)
###################### DETALHAR CRONOGRAMA
driver.maximize_window()
buscaFaturamento = driver.find_element(By.ID, "inputPesquisar").send_keys("Faturamento")
busca = driver.find_element(By.XPATH, '//*[@id="71"]/a/span')
busca.click()

time.sleep(10)

grupoFaturamento = driver.find_element(By.NAME, "grupoFaturamento")
selectUnidade = Select(grupoFaturamento)
selectUnidade.select_by_value('1439')

periodicidade = driver.find_element(By.NAME, "periodicidade")
selectUnidade = Select(periodicidade)
selectUnidade.select_by_value('3')

status = driver.find_element(By.ID, "situacao")
selectUnidade = Select(status)
selectUnidade.select_by_value("Em Andamento")
time.sleep(10)
#mesAnoFaturamentoInicial = driver.find_element(By.XPATH, '//*[@id="mesAnoFaturamentoInicial"]')
#options.set_preference('javascript.enabled', False)
time.sleep(5)
#mesAnoFaturamentoInicial.click()
#mesAnoFaturamentoInicial.send_keys("12/2024")


time.sleep(10)


####### DATA FINAL
#mesAnoFaturamentoFinal = driver.find_element(By.ID, "mesAnoFaturamentoFinal")
#options.set_preference('javascript.enabled', False)
time.sleep(5)
#mesAnoFaturamentoFinal.click()
#mesAnoFaturamentoFinal.send_keys("12/2024")

#options.set_preference('javascript.enabled', True)
botaoPesquisar = driver.find_element(By.ID, "botaoPesquisar").click()
time.sleep(30)
###################### DETALHAR CRONOGRAMA



#selecionar = driver.find_element(By.ID, "checkboxChavesPrimarias5036").click()
c11 = driver.find_element(By.XPATH, '//*[@id="cronograma"]/tbody/tr/td[3]/a').click()

time.sleep(80)
consistirLeitura = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[9]/a")
time.sleep(30)
consistirLeitura.click()


####### executar processos
#modulo = driver.find_element(By.ID, "idModulo")

#modulo2 = Select(modulo)
#modulo2.select_by_value("2")
# grupoFaturamento = driver.find_element(By.ID, "idGrupoFaturamento")
# grupoFaturamento2 = Select(grupoFaturamento)
# grupoFaturamento2.select_by_value("1439")


#processo = driver.find_element(By.ID, "idOperacao")

#processo2 = Select(processo)
#processo2.select_by_value("21")
time.sleep(20)
selecionarRota = driver.find_element(By.ID, "rotasSelecionadas")
selecionarRota2 = Select(selecionarRota)
selecionarRota2.select_by_value('177')




email = driver.find_element(By.XPATH, '//*[@id="emailResponsavel"]')

email.send_keys("francisco.pereira@qintess.com;carolbanza@gmail.com")

botaoExecutar = driver.find_element(By.ID, 'botaoExecutar')

botaoExecutar.click()



time.sleep(20)

header = driver.find_element(By.ID,"botaoExecutar")
scheight = .1
while scheight < 45.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
    
driver.save_full_page_screenshot('consistirLeitura2.png') 
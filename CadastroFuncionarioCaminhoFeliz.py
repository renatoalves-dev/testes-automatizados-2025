
################################ DEPENDÊNCIAS E LIB's ############################################################

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager   
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

################## Inicializando o  SELENIUM WED DRIVER NO CHROME ##############################


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o URL da GGAS

driver.get("http://ggas.copergas.com.br/ggas-teste-qintess")




title = driver.title
print(title)

# Encontrando a caixa de Login e realizando uma ação

login = driver.find_element(By.ID, "login")
senha = driver.find_element(By.ID, "senha")
button = driver.find_element(By.ID, "button3")

# setando valores no form de Login

login.send_keys("caroline")
senha.send_keys("Admin123")


button.click()

driver.fullscreen_window()
time.sleep(10)

busca = driver.find_element(By.ID, "inputPesquisar")
time.sleep(10)
busca.send_keys("Funcionário")
time.sleep(10)
href_funcionario = driver.find_element(By.LINK_TEXT, "Funcionário")

href_funcionario.click()

time.sleep(10)

################ Automatizar o <form/> Funcionários selecionando Funcionário  no LINK #######################

# href_funcionario = driver.find_element(By.LINK_TEXT, "Funcionário")
# href_funcionario.click()

# time.sleep(10)

driver.fullscreen_window()

time.sleep(10)

# Fechando o navegador
#driver.quit()




################################ Funcionário cadastro e pesquisa e exclusão ##############################


#  *************     PESQUISA DISABLED

nome = driver.find_element(By.ID, "nome")
nome.send_keys("Afranio Barbosa")
buttoPesquisar = driver.find_element(By.XPATH, '//*[@id="botaoPesquisar"]')
buttoPesquisar.click()
time.sleep(10)
driver.fullscreen_window()
time.sleep(10)

## ****************** inicio cadastro Funcionário

buttonIncluir = driver.find_element(By.NAME, "buttonIncluir")
buttonIncluir.click()
driver.fullscreen_window()
time.sleep(20)
nome = driver.find_element(By.ID, "nome")
nome.send_keys("Caroline Barbosa @TestesAutomatizadosQintess")
matricula = driver.find_element(By.ID, "matricula")
matricula.send_keys("202060")
descricao = driver.find_element(By.ID, "descricaoCargo")
descricao.send_keys("@testesAutomatizados dia 05/12/2024 SeleniumWeb")
ddd = driver.find_element(By.ID, "codigoDDD")
ddd.send_keys(61)
telefone = driver.find_element(By.ID, "telefone")
telefone.send_keys(992314219)
email = driver.find_element(By.ID, "email")
email.send_keys("caroline.banza@qintess.com")
empresaSelect = driver.find_element(By.ID, "idEmpresa")
selectEmpresa = Select(empresaSelect)
selectEmpresa.select_by_index(6)
time.sleep(20)
unidadeOrganizacional = driver.find_element(By.ID, "idUnidadeOrganizacional")
selectUnidade = Select(unidadeOrganizacional)
selectUnidade.select_by_value('61')
time.sleep(10)
buttonSalvar = driver.find_element(By.NAME, "ButtonSalvar")
buttonSalvar.click()
driver.fullscreen_window()
time.sleep(50)

############################## COMEÇANDO A AÇÃO DE REMOVER FUNCIONÁRIO CADASTRADO ##################

caixa = driver.find_element(By.XPATH, '//*[@id="funcionario"]/tbody/tr/td[1]/input')
caixa.click()
time.sleep(10)

buttoRemover = driver.find_element(By.NAME, "buttonRemover")
buttoRemover.click()
time.sleep(30)

#################### JAVASCRIPT CONFIRMAR ALERT() DE EXCLUSÃO DE FUNCIONÁRIO #########################################


WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.fullscreen_window()



time.sleep(40)

###### FECHANDO O NAVEGADOR

driver.quit()



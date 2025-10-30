
""""
Teste de Apresentação da Automação na Review:
 
1) Pesquisa um CPF válido e tentar alterar o CPF para inválido;
2) Pesquisar um Usuário, apagar o cadastro;
3) Cadastrar o mesmo Usuário deletado anteriormente.

criar uma Branch de Testes Automatizados

"""



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o GGAS
driver.get("https://ggas.copergas.com.br/ggas-teste-qintess")



title = driver.title
print(title)

# Encontrando a caixa de pesquisa e realizando uma ação

login = driver.find_element(By.ID, "login")
senha = driver.find_element(By.ID, "senha")
button = driver.find_element(By.ID, "button3")

# setando valores no form

login.send_keys("caroline.qintess")
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

###################################### Automatizar o <form Funcionários selecionando Funcionário  no LINK #######################

# href_funcionario = driver.find_element(By.LINK_TEXT, "Funcionário")
# href_funcionario.click()

# time.sleep(10)

driver.fullscreen_window()

time.sleep(10)

# Fechando o navegador
#driver.quit()




################################ Funcionário cadastro e pesquisa ###############################################################

##################### PESQUISA NA TABELA
# #nome = driver.find_element(By.ID, "nome")
# #nome.send_keys("Afranio Barbosa")
# matricula = driver.find_element(By.ID, "matricula")
# descricao = driver.find_element(By.ID, "descricaoCargo")
# empresa = driver.find_element(By.ID, "idEmpresa")
# unidade = driver.find_element(By.ID, "idUnidadeOrganizacional")
# habilitado = driver.find_element(By.ID, "habilitado")
#button = driver.find_element(By.ID, "botaoPesquisar")


################ BOTÃO INCLUIR FUNCIONÁRIO

buttonIncluir = driver.find_element(By.NAME, "buttonIncluir")
buttonIncluir.click()
time.sleep(20)
driver.fullscreen_window()
time.sleep(10)






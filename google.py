from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# definindo que usaremos o Firefox sem carregar a página graficamente
options = webdriver.FirefoxOptions()

# carregando uma página da Internet via Firefox
driver = webdriver.Firefox(options=options)
driver.get('http://google.com.br')

print("Página carregada.")
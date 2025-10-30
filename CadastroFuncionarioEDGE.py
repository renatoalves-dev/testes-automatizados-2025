import os
import re
import subprocess
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class CadastroFuncionarioEDGE():
  
  def test_basic_options():
     
   options = webdriver.EdgeOptions()
   driver = webdriver.Edge(options=options)

   options = webdriver.EdgeOptions()

   options.add_argument("--start-maximized")

   driver = webdriver.Edge(options=options)
   driver.get("https://ggas.copergas.com.br/ggas-teste-qintess")

    



def cadastroFuncionario():
    
  login = webdriver.find_element(By.ID, "login")
  senha = webdriver.find_element(By.ID, "senha")
  button = webdriver.find_element(By.ID, "button3")

# setando valores no form de Login

  login.send_keys("carol")
  senha.send_keys("Admin123")


  button.click()

  webdriver.fullscreen_window()
  

  

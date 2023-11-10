from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

options = Options()
options.headless = False #Excutar de forma visivel

##Acessando o navegador
navegador = webdriver.Chrome(options=options)

##Link para acessar o site
link= "https://idash.ifcshop.net/auth/realms/chat-bot-b2b/protocol/openid-connect/auth?client_id=chat-bot-b2b-app&redirect_uri=https%3A%2F%2Fidash.ifcshop.net%2F&state=7d3ac4d3-a588-4efe-acbd-8689666c8530&response_mode=fragment&response_type=code&scope=openid&nonce=ef238d2a-f304-4122-84b9-137299ed11ed"
navegador.get(url=link)
time.sleep(3)

##Inserindo usuario
inputUsuario = navegador.find_element(by=By.ID,value="username")
<<<<<<< HEAD
inputUsuario.send_keys("sophia.coelho")
=======

inputUsuario.send_keys("username")
>>>>>>> a31ed97523f082d80034b19087f9618cac602fda
time.sleep(5)

##Inserindo senha
inputSenha = navegador.find_element(by=By.ID,value="password")
inputSenha.send_keys("password")
time.sleep(5)

##Clicando no botão Sign In
buttonLogin = navegador.find_element(by=By.ID,value="kc-login")
buttonLogin.click()
time.sleep(5)

##Acessando a pagina quality
linkQ="https://idash.ifcshop.net/reports/attendance-quality"
navegador.get(url=linkQ)
time.sleep(5)

##Clicando no botão Selecionar todos
clickable = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(1) > div > div > button')
ActionChains(navegador)\
.click(clickable)\
.perform()
time.sleep(10)


##Variavel para pegar a data em D-1
data_ant = datetime.now() - timedelta(days=1)
data_ant_form = data_ant.strftime("%d/%m/%Y")

##Preenchendo data anterior quality
text_input = navegador.find_element(By.CSS_SELECTOR, "#\:r2\:")
ActionChains(navegador)\
.send_keys_to_element(text_input, data_ant_form)\
.perform()
time.sleep(10)

##Clicando no botão para gerar o relatório
GerarRelatorio = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.css-1a9w728 > button')
ActionChains(navegador)\
.click(GerarRelatorio)\
.perform()
time.sleep(10)


##Acessando a pagina Retenção    
linkR="https://idash.ifcshop.net/reports/subject"
navegador.get(url=linkR)
time.sleep(5)

##Clicando no botão Selecionar todos
clickable1 = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(1) > div > div > button')
ActionChains(navegador)\
.click(clickable1)\
.perform()
time.sleep(10)

##Preenchendo data anterior Retenção
text_input1 = navegador.find_element(By.CSS_SELECTOR, "#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(3) > div > div")
ActionChains(navegador)\
.send_keys_to_element(text_input1, data_ant_form)\
.perform()
time.sleep(10)

##Clicando no botão para gerar o relatório
GerarRelatorio1 = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.css-1a9w728 > button')
ActionChains(navegador)\
.click(GerarRelatorio1)\
.perform()
time.sleep(15)

##Acessando a pagina Tickets    
linkT="https://idash.ifcshop.net/reports/tickets"
navegador.get(url=linkT)
time.sleep(5)

##Clicando no botão Selecionar todos
clickable2 = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(1) > div > div > button')
ActionChains(navegador)\
.click(clickable2)\
.perform()
time.sleep(10)

##Preenchendo data anterior Tickets
text_input2 = navegador.find_element(By.CSS_SELECTOR, "#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(3) > div > div")
ActionChains(navegador)\
.send_keys_to_element(text_input2, data_ant_form)\
.perform()
time.sleep(10)

##Clicando no botão para gerar o relatório
GerarRelatorio2 = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.css-1a9w728 > button')
ActionChains(navegador)\
.click(GerarRelatorio2)\
.perform()
time.sleep(15)
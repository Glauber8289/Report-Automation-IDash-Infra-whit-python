from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import options
from selenium.webdriver.edge.options import Options
import time
from bs4 import BeautifulSoup as bs


options = Options()
options.headless = False #Excutar de forma visivel

navegador = webdriver.Edge(options=options)

link= "https://idash.ifcshop.net/auth/realms/chat-bot-b2b/protocol/openid-connect/auth?client_id=chat-bot-b2b-app&redirect_uri=https%3A%2F%2Fidash.ifcshop.net%2F&state=7d3ac4d3-a588-4efe-acbd-8689666c8530&response_mode=fragment&response_type=code&scope=openid&nonce=ef238d2a-f304-4122-84b9-137299ed11ed"

navegador.get(url=link)
time.sleep(3)


inputUsuario = navegador.find_element(by=By.ID,value="username")
inputUsuario.send_keys("sophia.coelho")
time.sleep(3)

inputSenha = navegador.find_element(by=By.ID,value="password")
inputSenha.send_keys("S0PH14@pires")
time.sleep(3)

buttonLogin = navegador.find_element(by=By.ID,value="kc-login")
buttonLogin.click()
time.sleep(3)


## Erro corrigir
##linkRelatorios = navegador.find_element(by=By.TAG_NAME, value= "SPAN")
##linkRelatorios.click
##time.sleep(3)


##linkRelatorios1 = navegador.find_element(by=By.TAG_NAME, value= "svg")
##linkRelatorios1.click
##time.sleep(2)

##linkQualidade = navegador.find_element(by=By.TAG_NAME,value="LI")
##linkQualidade.click
##time.sleep(2)

linkR="https://idash.ifcshop.net/reports/attendance-quality"

navegador.get(url=linkR)
time.sleep(5)


SelectAll = navegador.find_element (by=By.CSS_SELECTOR,value='#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(1) > div > div > button')
##SelectAll.click
print(SelectAll)
time.sleep(5)


##SelectAll = navegador.find_element (by=By.ID,value='root')
##SelectAll.click
##time.sleep(5)

###GeneratetAll = navegador.find_element (by=By.LINK_TEXT,value='')
##GeneratetAll.click
##time.sleep(5)

##inputD1 = navegador.find_element(by=By.ID,value=":rf:")
##inputD1.send_keys("07/11/2023")
##time.sleep(10)
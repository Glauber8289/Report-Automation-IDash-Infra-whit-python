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


options = Options()
options.headless = False #Excutar de forma visivel

navegador = webdriver.Chrome(options=options)

link= "https://idash.ifcshop.net/auth/realms/chat-bot-b2b/protocol/openid-connect/auth?client_id=chat-bot-b2b-app&redirect_uri=https%3A%2F%2Fidash.ifcshop.net%2F&state=7d3ac4d3-a588-4efe-acbd-8689666c8530&response_mode=fragment&response_type=code&scope=openid&nonce=ef238d2a-f304-4122-84b9-137299ed11ed"

navegador.get(url=link)
time.sleep(3)


inputUsuario = navegador.find_element(by=By.ID,value="username")

inputUsuario.send_keys("sophia.coelho")
time.sleep(5)

inputSenha = navegador.find_element(by=By.ID,value="password")
inputSenha.send_keys("S0PH14@pires")
time.sleep(5)




buttonLogin = navegador.find_element(by=By.ID,value="kc-login")
buttonLogin.click()
time.sleep(5)

#######################################################################

#Erro corrigir
##linkRelatorios = navegador.find_element(by=By.TAG_NAME, value= "SPAN")
##linkRelatorios.click
##time.sleep(3)

################################################################################


linkR="https://idash.ifcshop.net/reports/attendance-quality"

navegador.get(url=linkR)
time.sleep(5)








clickable = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div:nth-child(1) > div > div > button')
ActionChains(navegador)\
.click(clickable)\
.perform()
time.sleep(10)

text_input = navegador.find_element(By.CSS_SELECTOR, "#\:r2\:")
ActionChains(navegador)\
.send_keys_to_element(text_input, "08/11/2023")\
.perform()
time.sleep(10)

clickable1 = navegador.find_element(By.CSS_SELECTOR,value= '#root > div > main > div.MuiContainer-root.css-10ur324 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.css-1a9w728 > button')
ActionChains(navegador)\
.click(clickable1)\
.perform()
time.sleep(10)








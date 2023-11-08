from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless = False #Excutar de forma visivel

navegador = webdriver.Chrome(options=options)

link="https://idash.ifcshop.net/auth/realms/chat-bot-b2b/protocol/openid-connect/auth?client_id=chat-bot-b2b-app&redirect_uri=https%3A%2F%2Fidash.ifcshop.net%2F&state=7d3ac4d3-a588-4efe-acbd-8689666c8530&response_mode=fragment&response_type=code&scope=openid&nonce=ef238d2a-f304-4122-84b9-137299ed11ed"

navegador.get(url=link)
time.sleep(2)

inputUsuario = navegador.find_element(by=By.ID,value="username")
inputUsuario.send_keys("sophia.coelho")
time.sleep(2)

inputSenha = navegador.find_element(by=By.ID,value="password")
inputSenha.send_keys("S0PH14@pires")
time.sleep(2)

buttonLogin = navegador.find_element(by=By.ID,value="kc-login")
buttonLogin.click()
time.sleep(3)
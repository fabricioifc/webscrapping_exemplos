from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path=r'/home/fabricio/Desktop/geckodriver')
browser.get("https://sig.ifc.edu.br/sigaa/verTelaLogin.do") 
time.sleep(0.5)
username = browser.find_element_by_name("user.login")
password = browser.find_element_by_name("user.senha")
username.send_keys("fabricio.bizotto")
password.send_keys("NervosO11")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(1)

links = []
links.append(browser.find_element_by_link_text('Servidor'))
links.append(browser.find_element_by_link_text('Portal do Docente'))
links.append(browser.find_element_by_link_text('INA1246-2 - BANCO DE DADOS I - T01'))
links.append(browser.find_element_by_css_selector('.itemMenuHeaderAlunos:nth-child(1)'))
links.append(browser.find_element_by_css_selector('.itemMenuHeaderAlunos:nth-child(5)'))

for link in links:
	link.click()
	time.sleep(0.5)
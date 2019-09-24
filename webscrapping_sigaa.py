from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

executable_path = "/home/fabricio/Desktop/geckodriver"
browser = webdriver.Firefox(executable_path=executable_path)

browser.get("https://sig.ifc.edu.br/sigaa/verTelaLogin.do")

username_field = browser.find_element_by_name("user.login")
password_field = browser.find_element_by_name("user.senha")

username_field.send_keys("fabricio.bizotto")
password_field.send_keys("NervosO11")
password_field.send_keys(Keys.RETURN)

time.sleep(1)

browser.find_element_by_link_text('Servidor').click()
browser.find_element_by_link_text('Portal do Docente').click()
browser.find_element_by_link_text('INA1246-2 - BANCO DE DADOS I - T01').click()
browser.find_element_by_css_selector('.itemMenuHeaderAlunos:nth-child(1)').click()
browser.find_element_by_xpath('/html/body/div[1]/form/div/div/div[2]/div[3]/table/tbody/tr/td/a[5]').click()
browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[6]/div[2]/table/tbody/tr[2]/td[2]/a').click()

tabela = browser.find_element_by_css_selector('.tabelaRelatorio')

alunos = []
for linha in tabela.find_elements_by_xpath(".//tr"):
	colunas = linha.find_elements_by_xpath(".//td")
	if len(colunas) > 0:
		aluno = {
			'matricula': colunas[0].text,
			'nome': colunas[1].text,
			't1n1': colunas[2].text,
			't1r1': colunas[2].text,
			't1n2': colunas[2].text,
			't1r2': colunas[2].text,
		}
		alunos.append(aluno)

	print(alunos)
			
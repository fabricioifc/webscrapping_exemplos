import requests
import webbrowser
from bs4 import BeautifulSoup

URL_BASE = 'https://www.zoom.com.br'
URL_FIM = '/cata-pechincha'
STATUS_CODE = 200

def carregar_pagina():
	print('Baixando o conteúdo da página!')
	pagina = requests.get(URL_BASE + URL_FIM)
	print(pagina.status_code)
	if pagina.status_code == STATUS_CODE:
		conteudo = BeautifulSoup(pagina.content, 'html.parser')
		return conteudo
	raise Exception('Oops! Código {}. Não foi possível baixar a página. Verifique a URL informada!'.format(pagina.status_code))

def buscar_produtos(conteudo):
	return conteudo.find_all('li', class_='gallery-item')

def buscar_imagem(produto):
	imagem = produto.find('div', class_=['image-container']).find('img', class_=['not_product'])
	imagem_src = 'https:' + imagem['src']
	imagem_titulo = imagem['title']
	# webbrowser.open_new(imagem_src)
	return imagem_src, imagem_titulo

def buscar_percentual_desconto(produto):
	import re
	desconto = produto.find('span', class_=['discount-price-off']).get_text()
	return re.sub(r'[^0-9]', '', desconto)

def buscar_nome(produto):
	nome = produto.find('div', class_=['info-container']).find('span', class_='name-link')
	if nome is None:
		return None
	return nome.get_text()

def buscar_preco(produto):
	preco = produto.find('div', class_=['price-container']).find('span', class_='price-label')
	if preco is None:
		return None
	valor = preco.get_text()
	valor = valor.replace('R$ ', '')
	return valor

def buscar_parcelas(produto):
	parcelas = produto.find('div', class_=['price-container']).find('span', class_='price-parcel').find('span')
	if parcelas is None:
		return None
	return parcelas.get_text().strip()

def buscar_link_oferta(produto):
	oferta = produto.find('div', class_=['offer-container']).find('p', class_='lead').find('a')
	return URL_BASE + oferta['href']

def main():
	print('Vamos começar!')
	try:
		conteudo = carregar_pagina()
		produtos = buscar_produtos(conteudo)
		# produto = produtos[0]
		for produto in produtos:
			print(produto.prettify())
			print(buscar_imagem(produto))
			print(buscar_nome(produto))
			print(buscar_percentual_desconto(produto))
			print(buscar_preco(produto))
			print(buscar_parcelas(produto))
			print(buscar_link_oferta(produto))
	except Exception as e:
		raise e

main()
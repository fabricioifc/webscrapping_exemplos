import requests
import webbrowser
from bs4 import BeautifulSoup
import pandas

URL_BASE = 'https://www.zoom.com.br'
URL_PATH = '/cata-pechincha'
STATUS_CODE = 200

def carregar_pagina():
    print('Baixando o conteúdo da página!')
    pagina = requests.get(URL_BASE + URL_PATH)
    print(pagina.status_code)
    if pagina.status_code == STATUS_CODE:
        conteudo = BeautifulSoup(pagina.content, 'html.parser')
        # print(conteudo.prettify())
        return conteudo
    raise Exception('Oops! Código {}. Não foi possível baixar a página. Verifique a URL informada!'.format(
        pagina.status_code))


def buscar_produtos(conteudo):
    return conteudo.find_all('li', class_='gallery-item')

def buscar_imagem(produto):
    imagem = produto.find('div', class_=['image-container']).find('img')
    imagem_src = 'https:' + imagem['src']
    imagem_titulo = imagem['title']
    # webbrowser.open_new(imagem_src)
    return imagem_src, imagem_titulo

def buscar_percentual_desconto(produto):
    import re
    desconto = produto.find('span', class_=['discount-price-off']).get_text()
    return re.sub(r'[^0-9]', '', desconto)

def buscar_preco(produto):
    preco = produto.find('div', class_=['price-container']).find(class_='price-label')
    if preco is None:
        return None
    valor = preco.get_text()
    valor = valor.replace('R$ ', '')
    return valor

def buscar_parcelas(produto):
    parcelas = produto.find('div', class_=['price-container']).find('span', class_='price-parcel')
    if parcelas is None:
        return None
    return parcelas.find('span').get_text().strip()

def buscar_link_oferta(produto):
    link = produto.find('div', class_=['info-container']).find('a',class_='name-link')
    span = produto.find('div', class_=['info-container']).find('span',class_='name-link')

    if link is not None:
    	return URL_BASE + link['href']
    elif span is not None:
    	return URL_BASE + span['rel']
    return None

def criar_tabela_html(itens):
	dataframe = pandas.DataFrame(itens)
	dataframe.to_html(buf='produtos.html', escape=False, index=False)

def criar_imagem_tag(path):
	if path is None:
		return path
	return '<img src="'+ path + '" width="80" >'

def criar_link_tag(path):
	if path is None:
		return path
	return '<a target="_blank" href="{}">{}</a>'.format(path, 'Comprar')

def abrir_navegador():
	webbrowser.open_new_tab('produtos.html')

def main():
    print('Vamos começar!')
    try:
        conteudo = carregar_pagina()
        produtos = buscar_produtos(conteudo)
        # produto = produtos[0]
        print('Quantidade:', len(produtos))
        itens = []
        for produto in produtos:
        	# print(produto.prettify())
        	imagem = buscar_imagem(produto)
        	item = {
	            'imagem' : criar_imagem_tag(imagem[0]),
	            'titulo' : imagem[1],
	            'desconto' : buscar_percentual_desconto(produto),
	            'preco' : buscar_preco(produto),
	            'parcelas' : buscar_parcelas(produto),
	            'link' : criar_link_tag(buscar_link_oferta(produto))
            }
        	itens.append(item)
        criar_tabela_html(itens)
        abrir_navegador()
        print('Terminou!')
    except Exception as e:
        raise e

main()

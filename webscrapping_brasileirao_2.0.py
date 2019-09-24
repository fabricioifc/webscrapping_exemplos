import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# import lxml
import csv
import pandas
import inquirer

# Set the URL you want to webscrape from
csv_colunas = ['posicao','nome','escudo','pontos','jogos','vitorias','empates','derrotas','gp','gc','sg','ca','cv','aproveitamento','ultimos_jogos','proximo_jogo']
csv_nome = 'Tabela.csv'
tabela_nome = 'Tabela.html'


def get_entrada():
	pergunta1 = [
	  inquirer.List('serie',
	                message="Escolha uma Série.",
	                choices=['A', 'B', 'C', 'D'],
	            ),
	]
	resposta1 = inquirer.prompt(pergunta1)

	pergunta2 = [
	  inquirer.List('ano',
	                message="Escolha um Ano para a Série {0}".format(resposta1['serie']),
	                choices=list(reversed(range(2012,2020))),
	            ),
	]
	resposta2 = inquirer.prompt(pergunta2)
	return (resposta1['serie'].lower(), resposta2['ano'])


def main():

	entrada = get_entrada()

	# Connect to the URL
	url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-{}/{}'.format(entrada[0], entrada[1])
	print(url)
	response = requests.get(url.format(entrada[0], entrada[1]))

	# Parse HTML and save to BeautifulSoup object¶
	soup = BeautifulSoup(response.text, "html.parser")
	tabela = soup.find('table',{'class':'table m-b-20 tabela-expandir'})
	linhas = tabela.find_all('tr',{'class':'expand-trigger'})

	times = []
	for linha in linhas:
		colunas = linha.find_all(['td','th'])

		ultimos_jogos = []
		for x in colunas[12].find_all('span'):
			ultimos_jogos.append(x.text)

		time = {
			'posicao': colunas[0].find('b').text,
			'escudo': criarImagemTag(colunas[0].find('img',{'class':'icon escudo m-r-10'})['src']),
			'nome': colunas[0].find_all('span')[1].text,
			'pontos': colunas[1].text,
			'jogos': colunas[2].text,
			'vitorias': colunas[3].text,
			'empates': colunas[4].text,
			'derrotas': colunas[5].text,
			'gp': colunas[6].text,
			'gc': colunas[7].text,
			'sg': colunas[8].text,
			'ca': colunas[9].text,
			'cv': colunas[10].text,
			'aproveitamento': colunas[11].text,
			'ultimos_jogos': '-'.join(ultimos_jogos),
			'proximo_jogo': criarImagemTag(colunas[13].find('img')['src'])
		}
		times.append(time)

	criarTabelaHtml(times)
	salvarArquivo(times)

def salvarArquivo(times):
	try:
	    with open(csv_nome, 'w') as csvfile:
	        writer = csv.DictWriter(csvfile, fieldnames=csv_colunas, delimiter = ';')
	        writer.writeheader()
	        for data in times:
	            writer.writerow(data)
	except IOError:
	    print("I/O error")

# def baixarImagem(url):
# 	try:
# 		filename = url.split('/')[-1]
# 		r = requests.get(url, allow_redirects=True)
# 		with open('/tmp/'+filename, 'wb') as handler:
# 			handler.write(r.content)
# 	except Exception as e:
# 		raise e

def criarTabelaHtml(times):
	dataframe = pandas.DataFrame(times)
	dataframe.to_html(buf=tabela_nome, escape=False, index=False)

def criarImagemTag(path):
    return '<img src="'+ path + '" width="60" >'

main()
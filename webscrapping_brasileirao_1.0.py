import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# import lxml
import csv

# Set the URL you want to webscrape from
url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
tabela = soup.find('table',{'class':'table m-b-20 tabela-expandir'})

linhas = tabela.find_all('tr',{'class':'expand-trigger'})

times = []

for linha in linhas:
	indice = 0

	colunas = linha.find_all(['td','th'])
	imagem = colunas[indice].find('img',{'class':'icon escudo m-r-10'})['src']

	nome = colunas[indice].find_all('span')[1].text

	indice += 1
	pontos = colunas[indice].text
	indice += 1
	jogos = colunas[indice].text
	indice += 1
	vitorias = colunas[indice].text
	indice += 1
	empates = colunas[indice].text
	indice += 1
	derrotas = colunas[indice].text
	indice += 1
	gp = colunas[indice].text
	indice += 1
	gc = colunas[indice].text
	indice += 1
	sg = colunas[indice].text
	indice += 1
	ca = colunas[indice].text
	indice += 1
	cv = colunas[indice].text
	indice += 1
	aproveitamento = colunas[indice].text
	indice += 1

	ultimos_jogos = []
	for x in colunas[indice].find_all('span'):
		ultimos_jogos.append(x.text)
	indice += 1

	proximo_jogo = colunas[indice].find('img')['src']

	time = {
		'nome': nome,
		'escudo': imagem,
		'pontos': pontos,
		'jogos': jogos,
		'vitorias': vitorias,
		'empates': empates,
		'derrotas': derrotas,
		'gp': gp,
		'gc': gc,
		'sg': sg,
		'ca': ca,
		'cv': cv,
		'aproveitamento': aproveitamento,
		'ultimos_jogos': '-'.join(ultimos_jogos),
		'proximo_jogo': proximo_jogo
	}
	times.append(time)

csv_colunas = ['nome','escudo','pontos','jogos','vitorias','empates','derrotas','gp','gc','sg','ca','cv','aproveitamento','ultimos_jogos','proximo_jogo']
csv_nome = 'Tabela.csv'

try:
    with open(csv_nome, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_colunas, delimiter = ';')
        writer.writeheader()
        for data in times:
            writer.writerow(data)
except IOError:
    print("I/O error") 
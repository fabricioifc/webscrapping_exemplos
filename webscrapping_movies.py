#-*- coding: utf-8 -*-
 
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
 
def main():
 
    start = datetime.now()    
 
    url = 'https://www.indeed.com.br/empregos?q=vendedor&l=Videira,+SC&start=0'
    source = requests.get(url).text
 
    soup = BeautifulSoup(source, 'lxml')
     
    os.system('clear')
    print('-----' * 10)

    resultados = soup.find_all(class_=['clickcard', 'result']);
    for pagina in resultados:
    	try:
    		title = pagina.find(class_='title').text.strip()
    	except Exception as e:
    		raise e
    	print('Título:', title)


 
    # name = []
    # href = []
    # for x in soup.find_all('a', 'dl'):
    #     #print(x.get('download'))
    #     #print(x.get('download'), x.get('href'))
    #     name.append(x.get('download'))
    #     href.append(x.get('href'))
 
    # name.pop(0)
    # href.pop(0)
     
    # dirname = '/home/mikefromru/music/E-mantra/'
 
    # print('Download...')
    # numberSong = len(name)
    # i = 0
    # while i != len(name):
    #     e_url = requests.get(href[-1], stream=True)
    #     f = open(dirname + name[-1], 'wb')
    #     f.write(e_url.content)
    #     f.close()
    #     print(numberSong, '-', name[-1])
    #     href.pop()
    #     name.pop()
    #     numberSong -=1
 
    end = datetime.now()
    total = end - start
    print('The program was warking for {} min'.format(str(total)))
    print('done')
 
 
if __name__ == '__main__':
    main()
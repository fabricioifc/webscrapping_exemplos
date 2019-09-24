#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 

quotes=[] # a list to store quotes 

table = soup.find('div', attrs = {'id':'all_quotes'}) 
print(table)

if table != None:
	for row in table.findAll('div', attrs = {'class':'col-6'}): 
		quote = {} 
		quote['theme'] = row.h5.text 
		quote['url'] = row.a['href'] 
		quote['img'] = row.img['src'] 
		quote['lines'] = row.h5.text 
		quote['author'] = row.h5.text 
		quotes.append(quote) 

	print(quotes)
	filename = 'inspirational_quotes.csv'
	with open(filename, 'w') as f: 
		w = csv.DictWriter(f,['theme','url','img','lines','author']) 
		w.writeheader() 
		for quote in quotes: 
			w.writerow(quote) 

import requests
from lxml import html
from bs4 import BeautifulSoup

USERNAME    = 'fabricio.bizotto'
PASSSWORD   = 'NervosO11'
LOGIN_URL   = 'https://sig.ifc.edu.br/sigaa/verTelaLogin.do'
URL         = 'https://sig.ifc.edu.br/sigaa/ensino/consolidacao_customizada/detalhesTurma.jsf'

if __name__ == '__main__':
    session_requests = requests.session()
    logado = session_requests.get(LOGIN_URL)

# if __name__ == '__main__':
#     all_tweets = []
#     url = 'https://twitter.com/TheOnion'
#     data = requests.get(url)
#     html = BeautifulSoup(data.text, 'html.parser')
#     timeline = html.select('#timeline li.stream-item')
#     for tweet in timeline:
#         tweet_id = tweet['data-item-id']
#         tweet_text = tweet.select('p.tweet-text')[0].get_text()
#         all_tweets.append({"id": tweet_id, "text": tweet_text})
#         print(all_tweets) 
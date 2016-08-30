from bs4 import BeautifulSoup
import requests


def crawly(search, board):
    sourcecode = requests.get(r'http://boards.4chan.org/' +board+ r'/archive').text
    soup = BeautifulSoup(sourcecode, "html.parser")

    for link in soup.findAll('tr'):
        for tb in link.findAll('td', {'class': 'teaser-col'}):
            wew = str(tb.string)
            if search.lower() in wew.lower():
                print('\n' + wew)
                for linku in link.findAll('a', {'class': 'quotelink'}):
                    add = str(linku.get('href'))
                    print(r'http://boards.4chan.org' + add)

term = input("What do you want to search?")
board = input("Which board's archive?")
crawly(term, board)

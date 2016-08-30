from bs4 import BeautifulSoup
import requests


def crawly(search):
    sourcecode = requests.get('http://boards.4chan.org/a/archive').text
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
crawly(term)

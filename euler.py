import requests
from bs4 import BeautifulSoup

f = open("euler-questions.txt", "a", encoding="utf-8")

for i in range(1,784):
            url = f'https://projecteuler.net/minimal={i}'
            response = requests.get(url)
            text = response.text
            soup = BeautifulSoup(text)
            for data in soup(['style', 'script']):
                data.decompose()
            textNew = (' '.join(soup.stripped_strings))
            f.write('%s\n%s\n' % (url, textNew))
            if i % 100 == 0:
                print (i)
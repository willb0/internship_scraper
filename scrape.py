from bs4 import BeautifulSoup
import requests
import time
links = ['lever.co', 'greenhouse.io']

jobs = ['data science intern', 'data scientist intern',
        'software engineering intern', 'SWE intern',
        'data engineering intern', 'product intern', 'fastapi intern']
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def scrape(links,jobs):
    data = {}
    s = requests.session()
    for link in links:
        for job in jobs:
            url = 'https://www.google.com/search?q='
            kwds = '+'.join(job.split())
            r = s.get(f'{url}site%3A{link}+{kwds}')
            #print(r.content)
            soup = BeautifulSoup(r.text,'html.parser')
            links = [wrap.parent["href"] for wrap in soup.find_all('h3')]
            links = [link.split('&')[0].split('=')[1] for link in links]
            data.update(links)
    return data
scrape(links,jobs)

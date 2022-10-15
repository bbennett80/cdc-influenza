#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def get_img_urls():
    url = 'https://www.cdc.gov/flu/weekly/index.htm'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img', {'alt': 'INFLUENZA Virus Isolated'})[:2]
    img_urls = [f"https://www.cdc.gov{img.attrs['src']}" for img in imgs]
    return img_urls

urls = get_img_urls()

with open('README.md', 'w+') as f:
    f.write(f'''# cdc-influenza
CDC Weekly U.S. Influenza Surveillance Graphs

![Clinical Laboratories]({urls[0]}?raw=true)

![Public Health Laboratories]({urls[1]}?raw=true)
        ''')

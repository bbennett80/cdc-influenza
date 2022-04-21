#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def get_img_urls():
    url = 'https://www.cdc.gov/flu/weekly/index.htm'
    base_img_url = 'https://www.cdc.gov/'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img', {'alt': 'INFLUENZA Virus Isolated'})[:2]
    img_urls = [f"{base_img_url}{img.attrs['src']}" for img in imgs]
    return img_urls


def get_imgs(urls):
    for i in urls:
        print(i.replace('https://www.cdc.gov//flu/weekly/weeklyarchives2021-2022/images/', ''))
        r = requests.get(i)
        if r.status_code == 200:
            image = i.replace('https://www.cdc.gov//flu/weekly/weeklyarchives2021-2022/images/', '')
            with open(image, 'wb') as f:
                for img in r.iter_content(chunk_size=1024): 
                    f.write(img)


if __name__ == "__main__":
    urls = get_img_urls()
    get_imgs(urls)

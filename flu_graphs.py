#!/usr/bin/env python3
import requests
import os
from glob import glob
from bs4 import BeautifulSoup

def delete_old_gifs():
    gifs = glob('*.gif', recursive=True)
    if not gifs:
        print('No gifs to delete')
    else:
        for gif in gifs:
            os.remove(gif)
    return
        
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
    
    image_names = []
    
    for i in urls:
        r = requests.get(i)
        if r.status_code == 200:
            image = i.replace('https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/images/', '')
            image_names.append(image)
            with open(image, 'wb') as f:
                for img in r.iter_content(chunk_size=1024): 
                    f.write(img)
                    

    with open('README.md', 'w+') as f:
        f.write(f'''# cdc-influenza
CDC Weekly U.S. Influenza Surveillance Graphs

![Clinical Laboratories](https://github.com/bbennett80/cdc-influenza/blob/main/{image_names[0]})

![Public Health Laboratories](https://github.com/bbennett80/cdc-influenza/blob/main/{image_names[1]})
        ''')

    return        

if __name__ == "__main__":
    delete_old_gifs()
    urls = get_img_urls()
    get_imgs(urls)

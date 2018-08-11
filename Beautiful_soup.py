import requests
from bs4 import BeautifulSoup

archive_url = "http://www.idlebrain.com/movie/photogallery/maheshbabu23/index.html"

def get_img_urls():
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content,'html5lib')
    links = soup.findAll('a')

    img_links = [archive_url + link['href'] for link in links if link['href'].endswith('.jpg')]

    return img_links


print(get_img_urls())

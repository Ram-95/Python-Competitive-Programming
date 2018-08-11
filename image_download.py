#image download

import random
from urllib.request import Request, urlopen

def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    req = Request(image_url, headers={'User-Agent':'Mozilla/5.0'})

    urllib.request.urlretrieve(req,full_file_name)
    #print('Filename: {} Saved to computer '.format(full_file_name))
    print(req)



link = 'http://www.idlebrain.com/movie/photogallery/maheshbabu23/images/maheshbabu'
for i in range(30,50):
    full_link = link + str(i) + '.jpg'
    print(full_link)    
downloader(full_link)

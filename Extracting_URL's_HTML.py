#Parsing ECIL Careers Site

import requests
from bs4 import BeautifulSoup

#function to print the list
def print_list(l):
    for item in l:
        print(item)


headers = {
    'User-Agent': '<Name>',
    'From': '<email>'}


#Collecting the page from the server and parsing it
url = 'http://careers.ecil.co.in/login.php';
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html5lib')


#prettify() will format the html code in a tree structure
#print(soup.prettify())

images = []     #to store urls of the images
pdfs = []       #to store pdf urls
root = 'http://careers.ecil.co.in/'

# To get the src's from <img> tags and storing the urls in the list
for item in soup.findAll('img'):
    link = item.get('src')
    images.append(root + link)



# To get the href's from <a> tag and taking only the '.pdf' urls
for item in soup.findAll('a'):
    link = item.get('href')
    if link is None:
        continue
    else:
        if link[-4:] == '.pdf':
            pdfs.append(root+link)

print('Image URL\'s')
print('------------------------------------------------------------')
print_list(images)

print('\nPDF\'s URL\'s')
print('------------------------------------------------------------')
print_list(pdfs)


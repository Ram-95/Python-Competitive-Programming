# Mobile phones price alert program from amazon.in
# NOTE:  Only Moble phones price will be returned by this piece of code
# since the html code for all the mobile phones is same, this code works only
# for MOBILE PHONES only. Anything else will return 'ERRORS'

import bs4 as bs
import urllib.request

def get_price_amazon(url):
    #Importing necessary modules
    import bs4 as bs
    import urllib.request

    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    #getting the item name
    item_name = soup.title.string.split(':')

    # finding the price
    price = soup.find('span', id = 'priceblock_ourprice').text

    #cleaning the data
    price = price.split(' ')

    #Prices list -- type casted to integers
    price_list = []
    temp = price[-1].replace(',','')
    price_list.append(int(temp[:-3]))

    print("Current Price of \"{}\" is: Rs. {}/-".format(item_name[0],price[-1]))
    print(price_list)

my_phone_list = ['https://www.amazon.in/Redmi-Note-Onyx-Black-64GB/dp/B07PKTGR91/ref=sr_1_16?keywords=mobiles&qid=1552806931&s=gateway&sr=8-16',
                 'https://www.amazon.in/Apple-iPhone-Gold-32GB-Storage/dp/B0725RBY9V/ref=sr_1_2?keywords=Iphone&qid=1552808060&s=gateway&sr=8-2',
                 'https://www.amazon.in/Samsung-Galaxy-Black-Storage-Offer/dp/B07KWX9GNH/ref=sr_1_6?keywords=samsung+galaxy&qid=1552808125&s=gateway&sr=8-6',
                 'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B07DJD1Y3Q/ref=sr_1_1_sspa?crid=1JEEPDUJRNFDR&keywords=oneplus+6t+mobile&qid=1552808337&s=gateway&sprefix=one+plus%2Caps%2C291&sr=8-1-spons&psc=1',
                 'https://www.amazon.in/Motorola-XT1955-4-Moto-Power-Black/dp/B07NQGV37P/ref=sr_1_6?crid=15IMN24Y3M8I8&keywords=motorola+mobile&qid=1552808165&s=gateway&sprefix=motorola%2Caps%2C296&sr=8-6']
'''
for i in my_phone_list:
    get_price_amazon(i)
'''







url = 'https://www.amazon.in/Redmi-Note-Onyx-Black-64GB/dp/B07PKTGR91/ref=sr_1_16?keywords=mobiles&qid=1552806931&s=gateway&sr=8-16'

source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source, 'lxml')

#getting the name
item_name = soup.title.string.split(':')

# finding the price
price = soup.find('span', id = 'priceblock_ourprice').text

#cleaning the data
price = price.split(' ')

print("Current Price of \"{}\" is: Rs. {}/-".format(item_name[0],price[-1]))


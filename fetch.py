import requests
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('ferneture.csv', 'w', encoding='utf8')

# Set the URL you want to webscrape from
url = 'https://cushioncoversstore.com/collections/animal?page='

file = open('ferneture.json', 'w', encoding='utf8')

file.write('[\n')
data = {}
csv_columns = ['name', 'category', 'price', 'img']

writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()


for page in range(4):
    r = requests.get(url + str(page+1))
    soup = BeautifulSoup(r.content, "html.parser")

    ancher = soup.find_all(
        'div', {'class': "grid-product__content"})
   

    for pt in ancher:
        img = pt.find('img', {'class': 'lazyload grid__image-contain'})
        name= pt.find('div',{'class':'grid-product__title grid-product__title--body'})
        price=pt.find('div',{'class':'grid-product__price'})

    
        if (img!=None and name!=None and price!=None ):
            data['img'] = img['data-src']
            data['name']=name.text
            data['price']=price.text
            print( data['img'],'\n')
            print( data['name'],'\n')
            print( data['price'],'\n')
            json_data = json.dumps(data, ensure_ascii=False)
            
            
            file.write(json_data)
            file.write(",\n")
            writer.writerow({'img':data['img'], 'name':data['name'],'price': data['price'], 'category':'animal'})

file.write("\n]")
filecsv.close()
file.close()

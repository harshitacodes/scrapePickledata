import requests
import pprint
from bs4 import BeautifulSoup

URL = " https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.8682381&longitude=77.7129198" #url of the imdb.com 
sample = requests.get(URL)

soup = BeautifulSoup(sample.text,"html.parser")

def scrap_the_pickledata():
    div_tag = soup.find('div',class_ = "_1LZ3")
    div_tag1 = div_tag.find('div',class_ = '_3RA-')
    all_div = div_tag1.find_all('div',class_ = '_1fje')
    
    for dv in all_div:
        mDiv = dv.find_all('div',class_ = '_2i1r')
        for name in mDiv:

            href = name.find('div',class_ = '_3WhJ').a['href']
            link = 'https://paytmmall.com/' + href


            ndata = name.find('div',class_ = '_3WhJ')
            a_tag = ndata.find('a',class_ = '_8vVO')

            image_tag = a_tag.find('div',class_ = '_3nWP').img['src']

            div_tag = a_tag.find('div',class_ = 'pCOS')
            name_of_pickle = div_tag.find('div',class_ = '_2PhD').get_text()
            pickle_name.append(name_of_pickle)


            price = div_tag.find('div',class_ = '_2bo3')
            all_price = price.find('div',class_ = '_1kMS').span.get_text()
            price_of_pickle.append(all_price)


            picklesData = {}

            


        
        
alldata =scrap_the_pickledata()
print(alldata)
import requests
import pprint
from bs4 import BeautifulSoup
import pprint

URL = " https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.8682381&longitude=77.7129198" #url of the imdb.com 
sample = requests.get(URL)

soup = BeautifulSoup(sample.text,"html.parser")

def scrap_the_pickledata():
    table = soup.find('div',class_ = "_1LZ3")
    row = table.find('div',class_ = '_3RA-')
    pickles_data = row.find_all('div',class_ = '_1fje')
    
    for pickle in pickles_data:
        pickle_row = pickle.find_all('div',class_ = '_2i1r')
        for pickle_name in pickle_row:

            pickle_link = pickle_name.find('div',class_ = '_3WhJ').a['href']
            link = 'https://paytmmall.com/' + pickle_link

            single_pickle = pickle_name.find('div',class_ = '_3WhJ')
            image_tag = single_pickle.find('a',class_ = '_8vVO')
            image = image_tag.find('div',class_ = '_3nWP').img['src']
            # pprint.pprint(image)

            name_of_pickle = a_tag.find('div',class_ = 'pCOS')
            single_name = name_of_pickle.find('div',class_ = '_2PhD').get_text()
            # pprint.pprint(name_of_pickle)


            price_of_pickle = div_tag.find('div',class_ = '_2bo3')
            single_price = price_of_pickle.find('div',class_ = '_1kMS').span.get_text()
            # print(all_price)
        
        
alldata =scrap_the_pickledata()
# -*- coding: utf-8 -*-
"""
@author: Ajay Gautam M

"""

#Box Office Mojo Data Extraction


#Toto, I've a feeling we're not in Kansas anymore
import os
os.chdir('...\\data\\input.csv')

#Round up the usual suspects
import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import time
import pandas as pd

#It's not who I am underneath, but what I DO that DEFINES me
def scrape_bom_link(soup):
    l_header = soup.find('li', {'class': 'b_algo'})
    bom_link_tag = l_header.find('a')
    bom_link = bom_link_tag['href'] 
    return(bom_link)

def scrape_bom_data(rt_link):
    headers = {'User-Agent': 'Mozilla/5.0'}
    bom_res = requests.get(bom_link, headers=headers)
    bom_soup = BeautifulSoup(bom_res.text, 'html.parser')
    bom_tags = bom_soup.select('td > b')
    
    try:
        #Getting Domestic Total Gross
        bom_d = bom_tags[7].get_text()
        bom_domestic.append(bom_d)
    
    except(IndexError, ValueError, AttributeError, TypeError):
        bom_domestic.append(0)
        
    try:
        #Getting Worldwide Gross Total
        bom_w = bom_tags[10].get_text()
        bom_worldwide.append(bom_w)
    
    except(IndexError, ValueError, AttributeError, TypeError):
        bom_worldwide.append(0)
        
    try:
        #Getting the genre
        bom_g = bom_tags[2].get_text()
        bom_genre.append(bom_g)

    except(IndexError, ValueError, AttributeError, TypeError):
        bom_genre.append(0)
    
    try:
        #Getting the distributor
        bom_d = bom_tags[0].get_text()
        bom_distributor.append(bom_d)
    
    except(IndexError, ValueError, AttributeError, TypeError):
        bom_distributor.append(0)
            
    time.sleep(10)




#The Ring has awoken, it's heard its master's call
if __name__ == "__main__":
    
    #You talking to me?
    input_df = pd.read_csv('input.csv')
    
    #The Dude abides
    bom_domestic,bom_worldwide,bom_genre,bom_distributor = ([] for i in range(4))
        
    #Fasten your seatbelts. It's going to be a bumpy night.
    for name, year in zip(input_df.movie_name,input_df.year):
        response = requests.get("https://www.bing.com/search?q={0} box office mojo {1}".format(name, year))
        soup = BeautifulSoup(response.text, 'html.parser')
        bom_link = scrape_bom_link(soup)
        scrape_bom_data(bom_link)
    
    #What a dump
    input_df = input_df.join(pd.DataFrame({'domestic':bom_domestic,'worldwide':bom_worldwide,
                                           'genre':bom_genre, 'distributor':bom_distributor})) 
    
    input_df.to_csv("output.csv", sep=",", encoding = 'utf-8', index=False)

    print("Yippe-ki-yay, motherf***er!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
@author: Ajay Gautam M

"""

#Rotten Tomatoes Data Extraction

#Say "hello" to my little friend! 
import os
os.chdir('...\\data\\input.csv')

#Round up the usual suspects
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import pandas as pd

#It's not who I am underneath, but what I DO that DEFINES me
def scrape_rt_link(soup):
    l_header = soup.find('li', {'class': 'b_algo'})
    rt_link_tag = l_header.find('a')
    rt_link = rt_link_tag['href'] 
    return(rt_link)

def scrape_rotten_data(rt_link):
    headers = {'User-Agent': 'Mozilla/5.0'}
    rt_res = requests.get(rt_link, headers=headers)
    rt_soup = BeautifulSoup(rt_res.text, 'html.parser')
    
    try:
        #Getting critics average rating
        rt_avg_cr = rt_soup.find('div', class_="superPageFontColor").get_text()
        rt_avg_clean = int(''.join(filter(str.isdigit, rt_avg_cr)))
        rt_avg_cr_final = float('%.1f' %(rt_avg_clean/1000))
        avg_cr.append(rt_avg_cr_final)
        
    except(IndexError, ValueError, AttributeError, TypeError):
        avg_cr.append(0)
        
    
    try:
        #Getting the average users rating and Cleaning
        rt_avg_us = rt_soup.find('div', class_="audience-info hidden-xs superPageFontColor")
        rt_avg_us = rt_avg_us.find('div').get_text()
        rt_avg_us_clean = int(''.join(filter(str.isdigit, rt_avg_us)))
        rt_avg_us_final = float('%.1f' %(rt_avg_us_clean/100))
        avg_us.append(rt_avg_us_final)
    
    except(IndexError, ValueError, AttributeError, TypeError):
        avg_us.append(0)
        
        
    time.sleep(10)
    

#Well, here's another nice mess you've gotten me into!
if __name__ == "__main__":
    
    #Yo, Adrian!
    input_df = pd.read_csv('input.csv')
    
    #A martini. Shaken, not stirred
    avg_cr, avg_us = ([] for i in range(2))
    
    #I'm gonna make him an offer, he can't refuse
    for name, year in zip(input_df.movie_name,input_df.year):
        response = requests.get("https://www.bing.com/search?q={0} rotten tomatoes {1}".format(name, year))
        soup = BeautifulSoup(response.text, 'html.parser')
        rt_link = scrape_rt_link(soup)
        scrape_rotten_data(rt_link)
    
    #Leave the gun, Take the cannoli 
    input_df = input_df.join(pd.DataFrame({'rt_critic_score':avg_cr,
                                           'rt_audience_score':avg_us}))
    
    #There's no place like home
    input_df.to_csv("output.csv", sep=",", encoding = 'utf-8', index=False)
    
    print("Hasta la Vista, baby")
    
    

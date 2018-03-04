# -*- coding: utf-8 -*-
"""
@author: Ajay Gautam M

"""

#IMDB Data Extraction

#Here's Johnny!
import os
os.chdir('......\\data\\input.csv')

#Badges? We ain't got no badges! We don't need no badges! I don't have to show you any stinking badges!
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import pandas as pd

#It's not who I am underneath, but what I DO that DEFINES me
def find_new_url(base_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    new_url = soup.find('td', 'result_text').find('a').get('href')
    return new_url
    
def scrape_movie_data(parse_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(parse_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        #Getting the movie_year
        title_year = (soup.find('span',{ 'id' :'titleYear'}).find('a').get_text())
        year.append(title_year)
    
    except(IndexError, AttributeError, TypeError):
         year.append(0)
    
    try:
        #Getting the imdb rating
        rating = float(soup.find('span', {'itemprop': 'ratingValue'}).get_text())
        imdb.append(rating)
    
    except(IndexError, AttributeError, TypeError):
         imdb.append(0)
    
    try:
        #Getting the metacritic score
        meta_score = int(soup.find('div', class_="metacriticScore score_favorable titleReviewBarSubItem").get_text())
        meta.append(meta_score)
    
    except(IndexError, AttributeError, TypeError):
         meta.append(0)
    
    
    try:
        #Getting the certification
        certificate = soup.find('meta', {'itemprop':'contentRating'})
        certificate_final = certificate.attrs['content']
        cer.append(certificate_final)
    
    except(IndexError, AttributeError, TypeError):
         cer.append(0)
    
    try: 
        #Getting the runtime
        runtime_string = ''.join([r.get_text() for r in soup.select("div.txt-block > time")])
        runtime = int(''.join(filter(str.isdigit, runtime_string)))
        rtime.append(runtime)
   
    except(IndexError, AttributeError, TypeError, ValueError):
         rtime.append(0)
      
    time.sleep(20)


   

#Houston! We have a problem.
if __name__ == "__main__":
   
    #E.T Phone Home
    input_df = pd.read_csv('input.csv')
        
    #You're gonna need a bigger boat
    year, imdb, meta, cer, rtime = ([] for i in range(5))
   
    #Go ahead, Make my day...
    for row in input_df['movie_name']:
        base_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(row.split()) + '&s=all'
        parse_url = urljoin(base_url,find_new_url(base_url))
        scrape_movie_data(parse_url)
    
    #You complete me
    input_df = input_df.join(pd.DataFrame({'year':year,'imdb_rating':imdb,
                                           'meta_score':meta,
                                           'runtime':rtime,
                                           'certificate':cer}))
    
    #Chewie, we're home
    input_df.to_csv("output.csv", sep=",", encoding = 'utf-8', index=False)
        
    print("Frankly, my dear, I don't give a damn.")
    
    

 

    
    
    
    
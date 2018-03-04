# -*- coding: utf-8 -*-
"""
@author: Ajay Gautam M

"""

#Here's Johnny!
import os
os.chdir('C:\\Users\\AJAY GAUTAM\\Documents\\Oscar Cast')

#Oh, Jerry, don't let's ask for the moon. We have the stars
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd

#Rosebud
oscar_best_actor = requests.get("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor")

#Do-or do not. There is no try
oba_soup = BeautifulSoup(oscar_best_actor.content, 'html.parser')

#If you build it, he will come
actors =OrderedDict.fromkeys(['actor_name', 'href','oscar','movie_name'])

#Finding the table
table = oba_soup.find('table', attrs={'class': 'wikitable sortable'})
table

#Well, nobody's perfect.
prefix = 'https://en.wikipedia.org'
actors['actor_name'] = []
actors['href'] = []
actors['oscar'] = []
actors['movie_name'] = []

#Get busy living, or get busy dying
for row in table.find_all('tr')[1:]:
    actor_table = row.find_all('td')[0]
    if actor_table.find('b'):
            actors['oscar'].append(1)
    else:
            actors['oscar'].append(0)
    actor_name = actor_table.select('span.sorttext')
    for a in actor_name:
        try:
            actors['actor_name'].append(a.get_text())
            actors['href'].append(prefix + a.a['href'])
        except(TypeError):
            actors['actor_name'].append(" ")
            actors['href'].append(" ")    
    try:
        movie_table = row.find_all('td')[2]
        movie_name = movie_table.select('i')
        for m in movie_name:
            actors['movie_name'].append(m.get_text())
    except (IndexError):
        actors['movie_name'].append("")
    
#There's no place like home
actors_df = pd.DataFrame.from_dict(actors)
actors_df.to_csv("wiki_output_actors.csv", sep=",", encoding = 'utf-8', index=False)

#La-dee-da, la-dee-da.
if __name__ == "__main__":
    
    print("I'll be back")
    
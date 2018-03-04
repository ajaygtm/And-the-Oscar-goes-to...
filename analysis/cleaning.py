# -*- coding: utf-8 -*-
"""
@author: Ajay Gautam M

"""

import os
os.chdir('....\\data\\input.csv')

import pandas as pd
import_file = pd.read_csv('input.csv')


#RUNTIME
for index, run in enumerate(import_file['runtime']):
    str_run = str(run)
    if len(str_run)>3:
        str_run = str_run[:3]
    import_file['runtime'][index] = int(str_run)
    

#DOMESTIC
from decimal import Decimal
from re import sub

for index, dec in enumerate(import_file['domestic']):
    import_file['domestic'][index] = Decimal(sub(r'[^\d.]', '', dec))
    

#WORLDWIDE
for index, money in enumerate(import_file['worldwide']):
    if money.find('Â') > -1:
        import_file['worldwide'][index] = import_file['domestic'][index]
    elif money.find('e') > -1:
        import_file['worldwide'][index] = import_file['domestic'][index]
    else:
        import_file['worldwide'][index] = Decimal(sub(r'[^\d.]', '', money))
        
       
#Rotten_Tomatoes Critic Score
for index, score in enumerate(import_file['rt_critic_score']):
    if score < 1 :
        import_file['rt_critic_score'][index] = score*10
   
    
#Rotten_Tomatoes Audience Score
for index, score in enumerate(import_file['rt_audience_score']):
    if score == 0.5:
        import_file['rt_audience_score'][index] = 4
    elif score == 0.4:
        import_file['rt_audience_score'][index] = 3.9
    elif score == 4:
        import_file['rt_audience_score'][index] = 3.9
    elif score == 0.3:
        import_file['rt_audience_score'][index] = 3
        

#Genre
#Checking unique values
import_file.genre.unique()
import_file.genre.value_counts()

#So many sub genres are there. So they are grouped using the following function.

#Example - Genre Grouping
#Grouping is done for other sub-genres
for index, g in enumerate(import_file['genre']):
    if g.find("Sci-Fi")!= -1:
        import_file['genre'][index] = "Sci-Fi"


for index, g in enumerate(import_file['genre']):
    if g.find("Comedy")!= -1:
        import_file['genre'][index] = "Comedy"























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
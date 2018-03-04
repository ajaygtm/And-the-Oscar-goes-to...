# Data Extraction

The data used for this project is scraped from the following websites.
 * Wikipedia
 * IMDB
 * Rotten Tomatoes
 * Box Office Mojo

# Features

The required features or attributes scraped from the above websites are listed below. 

Feature name | Description | Source
---------    | ----------- | ------
imdb_rating  | IMDB rating | IMDB
meta_score   | Metacritic rating | IMDB
certificate  | Film Certification | IMDB
runtime  | Movie Runtime | IMDB
rt_audience_score|Rotten Tomatoes - Audience Average Rating | Rotten Tomatoes
rt_critic_score|Rotten Tomatoes - Critic Average Rating | Rotten Tomatoes
distributor | Movie Distributor | Box Office Mojo
genre | Movie Genre | Box Office Mojo
domestic | Domestic Box Office Collection | Box Office Mojo
worldwide | Worldwide Box Office Collection | Box Office Mojo  

## Awards
A strong indicators to "Oscar Success" are the other movie awards presented in the weeks preceding the Academy awards. So, for this project, the following awards are considered. 

Feature name | Award Name 
-------------| ---------- 
oscar | Academy Awards
critics_choice | Critics Choice Awards
sag | Screen Actors Guild
bafta | British Academy Film Awards
pga | Producers Guild of America
dga | Directors Guild of America
wga | Writers Guild of America
satellite | Satellite Awards
nbr | National Board of Review


### Note:
The data pertaining to the awards listed above is extracted from Wikipedia. 

### Another Note..
Since, the HTML structure/CSS selectors for the required data varies depending on the wikipedia pages, a unique code is not provided for scraping Wikipedia.

### Another Note...
Okay, this is the last note. 
I have provided a sample code used in this project for scraping the wikipedia page.



















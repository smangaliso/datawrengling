import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


# Request for the HTML response using the URL
url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
response = requests.get(url)

# Parse data from the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Inspect page to get the class name of the table
table_class = "wikitable sortable jquery-tablesorter"
road_safety_table = soup.find('table', {'class': "wikitable"})

# converting wiki table to dataframe
df = pd.read_html(str(road_safety_table))
df = pd.DataFrame(df[0])

# drop the unwanted columns
df = df.drop(['Road Network Length (in km) in 2013[29]', 'Number of People Killed per Billion km[30]',
              'Number of Seriously Injured in 2017/2018[30]'], axis=1)

# rename columns for ease
df = df.rename(columns={'Area (thousands of km2)[24]': 'Area', 'Population in 2018[25]': 'Population',
                        'GDP per capita in 2018[26]': 'GDP per capita',
                        'Population density (inhabitants per km2) in 2017[27]': 'Population density',
                        'Vehicle ownership (per thousand inhabitants) in 2016[28]': 'Vehicle ownership',
                        'Total Road Deaths in 2018[30]': 'Total Road Deaths',
                        'Road deaths per Million Inhabitants in 2018[30]': 'Road deaths per Million Inhabitants'})
# add column
year = [2018] * len(df)

df['year'] = year

# sort data
df = df.sort_values('Road deaths per Million Inhabitants')

#plot country with most deaths per million capita





# export to CSV
df.to_csv('Road_safety_in_Europe.csv', index=False)



if __name__ == '__main__':
    pass

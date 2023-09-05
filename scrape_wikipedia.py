# import Python libraries to be used
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# open the webpage assigned to the 'url' variable
page = requests.get(url)

# parse the webpage
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[1] # pick the second table from the webpage

titles = table.find_all('th') # pick the table column titles

headers = [title.text.strip() for title in titles] # create column headers from the titles

df = pd.DataFrame(columns=headers) # load the headers into a Pandas dataframe

column_data = table.find_all('tr') # find the data from the rows corresponding to each of the columns

for row in column_data[1:]: # start from the second row to avoid the empty list at index 0
    row_data = row.find_all('td') 
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

# write the dataframe to a csv format file
df.to_csv(r'/home/jerome/code/my_datasets/top_100_us_companies_by_revenue.csv', index=False)
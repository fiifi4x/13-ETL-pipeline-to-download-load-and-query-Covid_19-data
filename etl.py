import csv
import requests
import pandas as pd
import psycopg2
import boto3
from io import StringIO
from bs4 import BeautifulSoup
from util import database_connection

#extracting csv file from url

# covid_19 = pd.read_csv('covid_19_data.csv')
# #print(covid_19.head())
# table = 'covid_19_data'
# covid_19.to_sql(table, con=database_connection(), if_exists='replace', index=False)
# print('data successfully loaded into postgres')

covid_data = pd.read_sql('covid_19_data')
print(covid_data.head())

# url = 'https://drive.google.com/file/d/1SzmRIwlpL5PrFuaUe_1TAcMV0HYHMD_b/view'

# response = requests.get(url)
# response_content = response.content   #parser, search or find element, select table number, 
# soup = BeautifulSoup(response_content, 'lxml')
# table = soup.find_all('tables')
# print(table)
# selected_element = soup.find_all('table')
# table_number = selected_element[0]
# # stringigy table
# # select dataframe in table
# selectdf = table_number()




#print('dataframe ready')

#try:
# response = requests.get(url)
# cr = response.content
# print(cr)
# df = pd.DataFrame(cr)
# print('df successful')
#print(cs)
# r = response.content
# print(r)
#if response.status_code == '200':
#print('response successful')

# my_csv = pd.read_csv(url)
# print('csv in dataframe format')
# print(my_csv)

#else:
#print('response cannot be fetched')
#except:
#print('response cannot be printed')
# extract()

# Load dataframe to postgres

def load():
    table_name = 'covid_19_test'
    dfs.to_sql('alpha', con = database_connection(), if_exists = 'replace', index = 'false')
    print('ab sent to postgres')
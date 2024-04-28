import pandas as pd
import json
import psycopg2
# from etl import extract
# from etl import load
# from util import database_connection

# extract()
# load()

# simple df with rows and columns

# all_columns = 
# columns_needed = ['animals', 'boys', 'girls']

#removing index

# df = {
# 'africa':['ghana','nigeria','congo'],
# 'asia':['china', 'korea','japan']
# }
# print(pd.DataFrame(df), index=False)


# df = {
# 'names':['kofi','Kwesi','Mary'],
# 'age':['23','16','45'],
# 'sex':['Male','Male','Female']
# }
# print(pd.DataFrame(df))


df = pd.DataFrame(
{'name':'kofi','age':'34','tribe':'ga'},
{'name':'abeiku','age':('67','89','45'),'tribe':'fante'},
{'name':'kwesi','age':'54','tribe':'asante'}
)

dfjson = df.to_json('output.json')
#print('json converted')

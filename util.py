import psycopg2
from sqlalchemy import create_engine
from dotenv import dotenv_values
dotenv_values()

def database_connection():
    config = dotenv_values('.env')
    db_name = config.get("db_name")
    db_password = config.get('db_password')
    db_user = config.get('db_user')
    db_host = config.get('db_host')
    db_port = config.get('db_port')
    return create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')




import pandas as pd
from creds import database_info, database_string
from sqlalchemy import create_engine, inspect
import psycopg2

class Database:
    def __init__(self, database_info=database_info, database_string=database_string):
        self.database_info = database_info
        self.database_string = database_string

    def pull_dataset(self, name_of_table):
        conn_string = self.database_string
        # create the connection engine
        engine = create_engine(conn_string)
        # load the data into a pandas dataframe
        df = pd.read_sql_table(name_of_table, engine)
        return df
    
    def list_tables(self):
        # create the connection string to the database
        conn_string = self.database_string
        # create the connection engine
        engine = create_engine(conn_string)
        # create an inspector object
        inspector = inspect(engine)
        # get a list of all tables
        tables = inspector.get_table_names()
        # print the list of tables
        return print(tables)
    
    def drop_table(self, table_name):
        conn = psycopg2.connect(database_string)
        cur = conn.cursor()
        cur.execute('DROP TABLE ' + table_name + ";")
        conn.commit()
        cur.close()
        conn.close
        return

    def truncate_table(self, table_name):
        conn = psycopg2.connect(database_string)
        cur = conn.cursor()
        cur.execute('TRUNCATE TABLE ' + table_name + ";")
        conn.commit()
        cur.close()
        conn.close
        return
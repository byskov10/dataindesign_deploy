import pandas as pd
from creds import database_info, database_string
from sqlalchemy import create_engine

class Database:
    def __init__(self, database_info=database_info, database_string=database_string):
        self.database_info = database_info
        self.database_string = database_string

    def pull_dataset(self, name_of_table):
        conn_string = database_string
        # create the connection engine
        engine = create_engine(conn_string)

        # load the data into a pandas dataframe
        df = pd.read_sql_table(name_of_table, engine)

        return df
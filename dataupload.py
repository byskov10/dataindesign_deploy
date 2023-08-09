import psycopg2
import pandas as pd
from creds import database_string

conn = psycopg2.connect(database_string)
cursor = conn.cursor()

for i in range(1, 25):
    filename = f"cleaned_datasets/P{i:02}_eye_movements_cleaned.tsv"
    tablename = f"P{i:02}_eye_movements_cleaned" # Creating unique table name for each file
    
    print(f"Processing {filename}...")
    
    # Creating a table for each file
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {tablename} (
        Unnamed INTEGER,
        ParticipantName TEXT,
        MediaName TEXT,
        MouseEvent TEXT,
        MouseX NUMERIC,
        MouseY NUMERIC,
        GazeX NUMERIC,
        GazeY NUMERIC,
        View TEXT,
        AOIMouse TEXT,
        AOIGaze TEXT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    
    # Reading data from TSV file
    data = pd.read_csv(filename, sep='\t')
    
    # Convert data to a list of tuples to be used in the INSERT query
    tuples = [tuple(x) for x in data.to_numpy()]

    # Comma-separated string with the required number of placeholders
    placeholders = ','.join(['%s'] * len(data.columns))
    
    # Insert the data into the newly created table
    insert_query = f"INSERT INTO {tablename} VALUES ({placeholders})"
    cursor.executemany(insert_query, tuples)

    conn.commit()
    print(f"Finished uploading {filename} into {tablename}.")

cursor.close()
conn.close()
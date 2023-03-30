import sqlite3
import pandas as pd

con = sqlite3.connect('social_network.db')
cur = con.cursor()
# SQL query to get all relationships
all_relationships_query = """
    SELECT person1.name, person2.name, start_date, type FROM relationships
    JOIN people person1 ON person1_id = person1.id
    JOIN people person2 ON person2_id = person2.id
    WHERE type = 'spouse';
   
"""
# Execute the query and get all results
cur.execute(all_relationships_query)

all_relationships = cur.fetchall()
con.close()
# Print sentences describing each relationship
for person1, person2, start_date, type in all_relationships:
    print(f'{person1} has been a {type} of {person2} since {start_date}.')

   
path_of_csv = "csvfile.csv"

def csv(all_relationships, path_of_csv):
    df = pd.DataFrame(all_relationships, columns=["person1", "person2", "start-date", "type"])
    df.to_csv(path_of_csv, index=False)

csv(all_relationships, path_of_csv)
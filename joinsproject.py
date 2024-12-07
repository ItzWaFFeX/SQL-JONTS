import sqlite3

database = 'database (1).sqlite'

conn = sqlite3.connect(database)

print("Connected!")

import pandas as pd

joined_left = pd.read_sql("""
    SELECT * FROM Player
    LEFT JOIN season
     ON player.Player_Id == season.Man_of_the_Series
""",conn)

joined_cross = pd.read_sql("""
       SELECT c.Country_Id, c.Country_name, ci.City_Name
       FROM Country c
       CROSS JOIN city ci
""",conn)

union = pd.read_sql("""
    SELECT Player_Name FROM Player
    UNION
    SELECT Team_Name FROM team
    
""",conn)

print(union
)
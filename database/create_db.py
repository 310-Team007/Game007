import sqlite3

conn = sqlite3.connect('database/game_data.db')

c = conn.cursor()

# creats a database table named player
# c.execute("""CREATE TABLE player (
#                 player_name text,
#                 health integer,
#                 score integer                
#             )""")

# creates a table for enemy
# c.execute("""CREATE TABLE enemy (
#                 enemy_type text,
#                 kills integer
#             )""")

# Delete a table from the data base
# c.execute("DROP TABLE player")


# inserts data into database
# c.execute("INSERT INTO player VALUES ('Bob', 10, 200)")
# c.execute("INSERT INTO player VALUES ('Bob', 20, 400)")

# deletes data in table
# c.execute("DELETE FROM player WHERE player_name='Bob'")

# c.execute("SELECT * FROM player WHERE player_name='Bob'")
# c.execute("SELECT score FROM player")
# c.execute("SELECT health FROM player")

# # return a row
# print(c.fetchall())

# commiting to the database
conn.commit()

# closing connection to database
conn.close()
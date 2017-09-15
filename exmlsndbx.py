import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Insert a row of data
# c.execute("INSERT INTO ids VALUES ('94748384')")
c.execute("DELETE FROM ids")
c.execute("SELECT * FROM ids")
ids = c.fetchall()
for id in ids:
    print(id[0])
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

conn.close()
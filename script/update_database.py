"""
Script to update the database
"""
import os
import PyMySQL

print 'Initializing database...'
db = PyMySQL.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="local")

cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tasks ( \
    id INT NOT NULL AUTO_INCREMENT, \
    name CHAR(100) NOT NULL, \
    closed INT NOT NULL, \
    PRIMARY KEY (id) \
);")

cur.execute("DELETE FROM tasks;")

cur.execute("INSERT INTO tasks (name, closed) VALUES ('Start learning Pyramid', 0);")
cur.execute("INSERT INTO tasks (name, closed) VALUES ('Do quick tutorial', 0);")
cur.execute("INSERT INTO tasks (name, closed) VALUES ('Have some beer!', 0);")

db.commit()
db.close()

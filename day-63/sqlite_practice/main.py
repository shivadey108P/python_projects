import sqlite3

db = sqlite3.connect("./day-63/sqlite_practice/books-collection.db")

cursor = db.cursor()

# cursor.execute(
#     "CREATE TABLE books (    \
#         id INTEGER PRIMARY KEY, \
#         title VARCHAR(250) NOT NULL UNIQUE, \
#         author VARCHAR(250) NOT NULL, \
#         rating FLOAT NOT NULL)"
#     )

cursor.execute("INSERT INTO books VALUES( \
    1 , 'Harry Porter' , 'J. K. Rowling', 9.3 \
    )")

db.commit()
# Python + sqlite3
udemy course section 35  
https://www.w3schools.com/sql/sql_syntax.asp  
https://docs.python.org/3/library/sqlite3.html  


## SQL and databases
SQL to język dzięki któremu możemy poruszać się po bazach danych.  
Najważniejsze komendy SQL:
```
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index
```



## Python syntax
Na początku importujemy moduł oraz podłączamy się do wybranej bazy danych:
```
import sqlite3
con = sqlite3.connect('example.db')
```
tworzymy cursor:
```
cur = con.cursor()
```
poprzez funkcje *execute()* możemy wywoływać komendy SQL:
```
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
```

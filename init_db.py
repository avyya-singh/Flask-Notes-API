import psycopg2

conn = psycopg2.connect(database="postgres", host="localhost", user="postgres", password="mysecretpassword", port="5432")
cur = conn.cursor()

cur.execute("CREATE TABLE if NOT EXISTS table1(id serial PRIMARY KEY, name VARCHAR(100), description varchar(1000));")
cur.execute("insert into table1 (name, description) values ('john', 'description1');")

conn.commit()
cur.close()
conn.close()
import psycopg2
from datetime import datetime as dt

hostname = 'localhost'
port_id = 5432
database = 'test'
username = 'postgres'
pwd = 'udupi'
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS links')

    create_Script = ''' CREATE TABLE IF NOT EXISTS links (
                            id INT PRIMARY KEY,
                            link VARCHAR(10000),
                            email VARCHAR(100),
                            price INT,
                            datee TIMESTAMPTZ)'''
    cur.execute(create_Script)
    Insert_Script = 'INSERT INTO links(id,link,email,price,datee) VALUES (%s,%s,%s,%s,%s)'
    insert_values = (1,'abc','bcd',43,dt.now())

    cur.execute(Insert_Script,insert_values)
    conn.commit()
except Exception as error:
    print('Error')

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
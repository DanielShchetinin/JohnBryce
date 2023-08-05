import psycopg2
import names
import time


conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "top_250_movies",
        user = "postgres",
        password ="postgres")

cur = conn.cursor()

num = 0 
while True:
    if num == 50:
        print(cur.rowcount)
        conn.close()
        break
    name = names.get_full_name()
    print(name)
    query = f"""
    INSERT INTO python_test
    ("name")
    VALUES('{name}')"""
    time.sleep(1)
    cur.execute(query)
    conn.commit()
    num+=1
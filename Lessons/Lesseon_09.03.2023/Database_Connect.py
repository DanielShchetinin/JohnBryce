import psycopg2

try:

    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "top_250_movies",
        user = "postgres",
        password ="postgres"
    )

    cur = conn.cursor()

    query = """
    select * from imdb_top
    where release_date = 2017;"""
    cur.execute(query)
    while True:
        db_version = cur.fetchone()
        if db_version == None:
            break
        print(db_version[0])

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("\nDatabase connection closed.\n")
        


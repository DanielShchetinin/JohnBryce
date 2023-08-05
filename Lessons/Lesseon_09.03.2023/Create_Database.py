import psycopg2

print("\n"*3)
movies_options = ["Find movie by Name", "Movies by Rating"]
movies_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(movies_options)])
print(movies_menu)
movies_options_choose = input("\nEnter a number: ")

if movies_options_choose == "1":
    print("\n"*25)
    movie_name: str = input("\nPlease enter the name of your choosed movie: ")
    
    with psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "top_250_movies",
        user = "postgres",
        password ="postgres") as conn:
    
        with conn.cursor() as cur:
            query = f"""
            SELECT * FROM imdb_top
            WHERE movie_name ilike %s
            """
            cur.execute(query, movie_name)
            result = cur.fetchone()
            if result == None:
                    print("\n"*25)
                    print("Your movie not in the top 250 IMDB movies.")
                    print("\n"*2)
                    exit()
            print("\n"*25)
            print("Movie name:", result[0], '\nRelease Year:', result[1], "\nIMDB Rating:", result[2], "\n"*2)

if movies_options_choose == "2":
    print("\n"*25)
    movie_rating = input("\nPlease enter the rating for view the movies:  ")
    print("\n"*25)
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "top_250_movies",
        user = "postgres",
        password ="postgres")
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM imdb_top;")
    num = 0
    while True:
        result = cur.fetchone()
        if result == None:
            print("\n"*2)
            print("Choosed movies:", num)
            print("\n")
            break
        if float(result[2]) >= float(movie_rating):
            print(result[0], result[1], result[2])
            num +=1
    conn.close()
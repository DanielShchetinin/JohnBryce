import psycopg2

def check_movie_exists(movie_name: str) -> bool:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="top_250_movies",
        user="postgres",
        password="postgres")

    query = """
    SELECT * FROM imdb_top
    WHERE movie_name ilike %s"""
    with conn:
        with conn.cursor() as cur:
            cur.execute(query, (movie_name,))
            result = cur.fetchone()
    return result


def main():
    try:
        movie_name = input("Enter the movie name: ")
        result_info = check_movie_exists(movie_name)
        print(result_info[0],result_info[1],result_info[2])

    except Exception as error:
        print("\nYour requisition failed:")
        print(error, "\n\n")
        main()


if __name__ == '__main__':
    main()

from datasource import Database
import massege_util
import config
import querie_constants as qc
from mysql.connector import Error


def insert_request(db, filter_field, keyword):
    db.insert_query(qc.save_request, params=(filter_field, keyword))


def save_request(filter_field):
    def decorator(func):
        def wrapper(*args):
            args_list = list(args)
            db = args_list.pop(0)
            res = func(db, *args_list)
            insert_request(db, filter_field, ", ".join([str(arg) for arg in args_list]))
            return res

        return wrapper

    return decorator


def get_ten_movies_by_rating(db: Database):
    return db.execute_query(qc.ten_movies_rating, (10,))


@save_request("title")
def search_movies_by_title(db, title):
    return db.execute_query(qc.movies_by_title, params=(f"%{title}%", 10))


@save_request("genre, year")
def search_movies_by_genre_and_year(db, genre, year):
    return db.execute_query(qc.movies_by_genre_and_year, params=(f"%{genre}%", year, 10))


@save_request("rating")
def search_movies_by_rating(db, rating):
    return db.execute_query(qc.movies_by_rating, params=(rating, 10))


@save_request("cast")
def search_movies_by_cast(db, cast):
    return db.execute_query(qc.movies_by_cast, params=(f"%{cast}%", 10))


@save_request("keyword")
def search_movies_by_keyword(db, keyword):
    return db.execute_query(qc.movies_by_keyword, params=(f"%{keyword}%", f"%{keyword}%", 10))


def get_popular_requests(db, limit):
    return db.execute_query(qc.popular_requests, params=(limit,))


def main():
    dbconfig = {
        'host': config.host,
        'user': config.user,
        'password': config.password,
        'database': config.database,
        'port': config.port,
        'use_pure': config.is_pure
    }
    db = Database(dbconfig)
    if db.connection is None:
        exit()
    first_movies = get_ten_movies_by_rating(db)
    massege_util.print_films(first_movies)
    while True:
        massege_util.print_commands()
        command = input("Your choice: ")
        try:
            if command == '1':
                title = input("Enter the movie title: ")
                movies = search_movies_by_title(db, title)
                massege_util.print_films(movies)

            elif command == '2':
                min_year = 2009
                max_year = 2016
                massege_util.print_genres()
                genre = input("Enter the genre:  ").strip().capitalize()
                if genre not in massege_util.genres:
                    print(f'Invalid genre entered. / Ungültiges Genre eingegeben')
                    continue
                year = input(f"Enter the year from {min_year} to {max_year}: ")
                if not year.isdigit():
                    print(f'Invalid data entered. /  Falsche Daten eingegeben')
                    continue
                year = int(year)
                if year < min_year or year > max_year:
                    print(f'Invalid data entered. /  Falsche Daten eingegeben')
                    continue
                movies = search_movies_by_genre_and_year(db, genre, year)
                massege_util.print_films(movies)

            elif command == '3':
                rating = input("Enter the rating (0 - 10):  ").strip()
                if not rating.replace(".", "", 1).isdigit():
                    print(f'Invalid rating entered. /  Falsche Rating eingegeben')
                    continue
                rating = float(rating)
                if not 0 <= rating <= 10:
                    print(f'Invalid rating entered. /  Falsche Rating eingegeben')
                    continue
                movies = search_movies_by_rating(db, rating)
                massege_util.print_films(movies)

            elif command == '4':
                cast = input("Enter the cast:  ").strip().capitalize()
                movies = search_movies_by_cast(db, cast)
                massege_util.print_films(movies)

            elif command == '5':
                keyword = input("Enter the keyword:  ").strip()
                movies = search_movies_by_keyword(db, keyword)
                massege_util.print_films(movies)

            elif command == '6':
                requests = get_popular_requests(db, 10)
                massege_util.print_requests(requests)

            elif command == '7':
                print("Exiting...")
                break

            else:
                print("Invalid command. Please try again.")
        except Error as e:
            print(f"Connection error/ Verbindungsfehler: {e}")
            break
    db.close()


if __name__ == '__main__':
    main()

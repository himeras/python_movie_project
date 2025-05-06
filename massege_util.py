from tabulate import tabulate
import textwrap

film_headers = ("Title", "Year", "Genres", "Cast", "Runtime", "Rating")
request_headers = ("Key", "Value", "Count")
genres = ["Action", "Comedy", "Sport", "Crime", "Drama", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller",
          "Family", "Fantasy", "History", "War", "Western", "Music", "Short", "Documentary", "Biography",
          "Adventure", "Animation"]


def wrap_cell(text, width):
    return "\n".join(textwrap.wrap(str(text), width=width))


def format_wrapped_table(data, widths):
    return [
        [wrap_cell(cell, width) for cell, width in zip(row, widths)]
        for row in data
    ]


def print_films(list_films):
    column_width = (30, 4, 30, 30, 7, 5)
    formatted_films = format_wrapped_table(list_films, column_width)
    if list_films:
        print(tabulate(formatted_films, film_headers, "grid"))
    else:
        print("+" * 100)
        print("No results found. / Keine Ergebnisse gefunden.")
        print("+" * 100)


def print_commands():
    print("Enter a command:")
    print("1. Search movies by title")
    print("2. Search movies by genre and year")
    print('3. Search movies by rating')
    print('4. Search movies by cast')
    print('5. Search movies by keyword')
    print("6. Show popular search queries")
    print("7. Exit")


def print_requests(list_requests):
    column_width = (40, 40, 10)
    formatted_requests = format_wrapped_table(list_requests, column_width)
    if list_requests:
        print(tabulate(formatted_requests, request_headers, "grid"))
    else:
        print("+"*100)
        print("No results found. / Keine Ergebnisse gefunden.")
        print("+"*100)


def print_genres():
    cols = 7
    rows = [genres[i:i + cols] for i in range(0, len(genres), cols)]
    if len(rows[-1]) < cols:
        rows[-1].extend([""] * (cols - len(rows[-1])))
    print(tabulate(rows, tablefmt="grid"))

lambda a, b: a + b

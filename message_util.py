from tabulate import tabulate
import textwrap

film_headers = ("Title", "Year", "Genres", "Cast", "Runtime", "Rating")
request_headers = ("Key", "Value", "Count")

emoji_map = {
        "Horror": "🧟", "Comedy": "😂", "Drama": "🎭", "War": "⚔️", "Sci-Fi": "👽",
        "Action": "💥", "Romance": "❤️", "Animation": "🎨", "Fantasy": "🧙",
        "Music": "🎶", "Sport": "⚽", "History": "📜", "Thriller": "🔪",
        "Mystery": "🕵️", "Western": "🤠", "Documentary": "🎥",
        "Adventure": "🧗", "Crime": "🚓", "Biography": "🧬", "Short": "⏱️",  "Family": "👨‍👩‍👧‍👦"
    }


def wrap_cell(text, width):
    return "\n".join(textwrap.wrap(str(text), width=width))


def format_wrapped_table(data, widths):
    return [
        [wrap_cell(cell, width) for cell, width in zip(row, widths)]
        for row in data
    ]


def print_error(title):
    print("+" * 100)
    print(f'Invalid {title} entered.')
    print("+" * 100)


def print_films(list_films):
    column_width = (30, 4, 30, 30, 7, 5)
    formatted_films = format_wrapped_table(list_films, column_width)
    if list_films:
        print(tabulate(formatted_films, film_headers, "rounded_grid"))
    else:
        print("+" * 100)
        print("No results found.")
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
        print(tabulate(formatted_requests, request_headers, "rounded_grid"))
    else:
        print("+" * 100)
        print("No results found.")
        print("+" * 100)


def print_genres():
    # Форматируем каждое значение с эмодзи и жанром, добавляя пробелы
    formatted = [f"{value} {key}" for key, value in emoji_map.items()]

    # Разбиваем на строки по 7 элементов
    rows = [formatted[i:i + 7] for i in range(0, len(formatted), 7)]

    # Печатаем в табличном формате с выравниванием по левому краю
    print(tabulate(rows, tablefmt="plain", colalign=("left",) * 7))



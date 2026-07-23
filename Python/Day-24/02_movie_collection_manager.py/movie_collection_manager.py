import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "movies.txt")
REPORT_FILE = os.path.join(SCRIPT_DIR, "movie_report.txt")
DATE_FORMAT = "%Y-%m-%d"

MIN_RATING = 0.0
MAX_RATING = 10.0


def load_movies():
    movies = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                movie_id, title, genre, rating, date_added = [part.strip() for part in line.split(",")]

                movies[movie_id] = {
                    "title": title,
                    "genre": genre,
                    "rating": float(rating),
                    "date_added": date_added
                }
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Data file is corrupted or contains invalid formats.")
    return movies


def save_movies():
    with open(DATA_FILE, "w") as file:
        for movie_id, info in movies.items():
            file.write(f"{movie_id}, {info['title']}, {info['genre']}, {info['rating']}, {info['date_added']}\n")


movies = load_movies()


def format_header(title, width=5):
    return f"{'=' * width} {title} {'=' * width}"


def find_movie(movie_id):
    return movies.get(movie_id)


def display_movie(movie_id, info):
    print(f"Movie ID: {movie_id}\nTitle: {info['title']}\nGenre: {info['genre']}\nRating: {info['rating']}\nDate Added: {info['date_added']}")
    print("-----------------")


def get_valid_movie_id():
    while True:
        movie_id = input("Enter Movie ID: ").strip()
        if not movie_id:
            print("Movie ID cannot be empty.")
            continue
        if movie_id in movies:
            print("Movie ID already exists.")
            return None
        return movie_id


def get_valid_title():
    while True:
        title = input("Enter Title: ").strip()
        if not title:
            print("Title cannot be empty.")
            continue
        return title


def get_valid_genre():
    while True:
        genre = input("Enter Genre: ").strip()
        if not genre:
            print("Genre cannot be empty.")
            continue
        return genre


def get_valid_rating():
    while True:
        try:
            rating = float(input("Enter Rating: "))
        except ValueError:
            print("Rating must be a number.")
            continue
        if rating < MIN_RATING or rating > MAX_RATING:
            print(f"Must be between {MIN_RATING} and {MAX_RATING}.")
            continue
        return rating


def add_movie():
    movie_id = get_valid_movie_id()
    if movie_id is None:
        return

    title = get_valid_title()
    genre = get_valid_genre()
    rating = get_valid_rating()
    date_added = datetime.now().strftime(DATE_FORMAT)

    movies[movie_id] = {"title": title, "genre": genre, "rating": rating, "date_added": date_added}
    save_movies()
    print("Movie added successfully.")


def view_movies():
    if not movies:
        print("Movie Collection is empty.\n")
        return
    for movie_id, info in movies.items():
        display_movie(movie_id, info)


def search_by_id():
    movie_id = input("Enter Movie ID: ").strip()
    info = find_movie(movie_id)
    if info is None:
        print("Movie not found.")
        return
    display_movie(movie_id, info)


def search_by_title():
    query = input("Enter Title: ").strip().lower()
    found = False
    for movie_id, info in movies.items():
        if query in info["title"].lower():
            display_movie(movie_id, info)
            found = True
    if not found:
        print("Movie not found.")


def search_movie():
    if not movies:
        print("Movie Collection is empty.\n")
        return
    while True:
        choice = input(
            f"\n{format_header('Search Movie')}\n"
            "1. Search by Movie ID\n"
            "2. Search by Title\n"
            "3. Back\n\n"
            "Enter your choice: "
        )

        if choice == "1":
            search_by_id()
        elif choice == "2":
            search_by_title()
        elif choice == "3":
            break
        else:
            print("Invalid Choice. Please pick 1-3.")


def rate_movie():
    movie_id = input("Enter Movie ID: ").strip()
    info = find_movie(movie_id)
    if info is None:
        print("Movie not found.")
        return

    rating = get_valid_rating()
    info["rating"] = rating
    save_movies()
    print("Rating updated successfully.")


def delete_movie():
    movie_id = input("Enter Movie ID: ").strip()
    if find_movie(movie_id) is not None:
        del movies[movie_id]
        save_movies()
        print("Movie deleted successfully.")
    else:
        print("Movie not found.")


def get_average_rating():
    return sum(info["rating"] for info in movies.values()) / len(movies)


def get_highest_rated_movie():
    movie_id = max(movies, key=lambda m: movies[m]["rating"])
    return movie_id, movies[movie_id]


def get_genre_counts():
    genres = {}
    for info in movies.values():
        genres[info["genre"]] = genres.get(info["genre"], 0) + 1
    return genres


def generate_report():
    if not movies:
        print("Movie Collection is empty.\n")
        return

    average_rating = get_average_rating()
    _, highest_info = get_highest_rated_movie()
    genres = get_genre_counts()

    with open(REPORT_FILE, "w") as file:
        file.write(f"{format_header('MOVIE REPORT', 10)}\n\n")
        file.write("Generated On:\n")
        file.write(f"{datetime.now().strftime(DATE_FORMAT)}\n\n")
        file.write("Total Movies:\n")
        file.write(f"{len(movies)}\n\n")
        file.write("Average Rating:\n")
        file.write(f"{average_rating:.2f}\n\n")
        file.write("Highest Rated Movie\n\n")
        file.write(f"Title: {highest_info['title']}\n")
        file.write(f"Rating: {highest_info['rating']}\n\n")
        file.write("--------------------------------\n\n")
        file.write("Movies Per Genre\n\n")
        for genre, count in sorted(genres.items()):
            file.write(f"{genre} : {count}\n")
        file.write("\n--------------------------------\n\n")
        file.write("Complete Movie List\n\n")
        file.write(f"{'ID':<8}{'Title':<25}{'Genre':<15}{'Rating':<8}{'Date Added'}\n\n")
        for movie_id, info in sorted(movies.items()):
            file.write(
                f"{movie_id:<8}{info['title']:<25}{info['genre']:<15}{info['rating']:<8}{info['date_added']}\n"
            )

    print("Movie report generated to movie_report.txt.")


while True:
    choice = input(
        f"{format_header('Movie Collection')}\n"
        "1. Add Movie\n"
        "2. View Movies\n"
        "3. Search Movie\n"
        "4. Rate Movie\n"
        "5. Delete Movie\n"
        "6. Generate Report\n"
        "7. Exit\n\n"
        "Enter your choice: "
    )

    if choice == "1":
        add_movie()
    elif choice == "2":
        view_movies()
    elif choice == "3":
        search_movie()
    elif choice == "4":
        rate_movie()
    elif choice == "5":
        delete_movie()
    elif choice == "6":
        generate_report()
    elif choice == "7":
        print("Thank you for using the Movie Collection Manager.")
        break
    else:
        print("Invalid Choice. Please pick 1-7.")

    print()

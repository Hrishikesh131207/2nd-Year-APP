import csv
import re

FILE_NAME = "movies.csv"


def load_movies():
    movies = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                movies.append(row)

    except FileNotFoundError:
        print(f"Error: {FILE_NAME} not found.")

    return movies


def display_movies(movies):
    if not movies:
        print("No movie records found.")
        return

    print("\n--- All Movie Information ---")

    for movie in movies:
        print(f"Movie ID : {movie['Movie ID']}")
        print(f"Title    : {movie['Title']}")
        print(f"Genre    : {movie['Genre']}")
        print(f"Year     : {movie['Year']}")
        print(f"Rating   : {movie['Rating']}")
        print("-" * 35)


def search_by_id(movies):
    movie_id = input("Enter Movie ID: ").strip()

    for movie in movies:
        if movie["Movie ID"] == movie_id:
            print("\n--- Movie Found ---")
            print(f"Movie ID : {movie['Movie ID']}")
            print(f"Title    : {movie['Title']}")
            print(f"Genre    : {movie['Genre']}")
            print(f"Year     : {movie['Year']}")
            print(f"Rating   : {movie['Rating']}")
            return

    print("Movie not found.")


def search_by_title(movies):
    title = input("Enter movie title to search: ").strip()

    pattern = re.compile(title, re.IGNORECASE)
    found = False

    for movie in movies:
        if pattern.search(movie["Title"]):
            print("\n--- Movie Found ---")
            print(f"Movie ID : {movie['Movie ID']}")
            print(f"Title    : {movie['Title']}")
            print(f"Genre    : {movie['Genre']}")
            print(f"Year     : {movie['Year']}")
            print(f"Rating   : {movie['Rating']}")
            print("-" * 35)
            found = True

    if not found:
        print("No movies found with that title.")


def main():
    movies = load_movies()

    while True:
        print("\n===== Movie Collection System =====")
        print("1. Display All Movies")
        print("2. Search Movie by Movie ID")
        print("3. Search Movie by Title")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(movies)

        elif choice == "2":
            search_by_id(movies)

        elif choice == "3":
            search_by_title(movies)

        elif choice == "4":
            print("Thank you for using the Movie Collection System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

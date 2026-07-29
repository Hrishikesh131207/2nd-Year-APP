class Movie:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price

    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("\nMovie Name :", self.name)
        print("Rating :", self.rating)
        print("Ticket Price :", self.price)
        print("Category :", self.category())


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self):
        name = input("Enter Movie Name: ")
        rating = float(input("Enter Rating (0-10): "))
        price = float(input("Enter Ticket Price: "))
        self.movies.append(Movie(name, rating, price))
        print("Movie Added Successfully!")

    def display_movies(self):
        if len(self.movies) == 0:
            print("No movies available.")
        else:
            i = 0
            while i < len(self.movies):
                self.movies[i].display()
                i += 1


cinema = Cinema()

while True:
    print("\n1. Add Movie")
    print("2. Display Movies")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cinema.add_movie()
    elif choice == 2:
        cinema.display_movies()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
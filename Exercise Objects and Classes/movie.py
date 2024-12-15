# Create a class Movie. The __init__ method should receive a name and a director.
# It should also have a default value of an attribute called watched set to False.
# There should also be a class attribute __watched_movies which will keep track of the number of all the watched movies.
# The class should have the following methods:

# · change_name(new_name: str) - changes the name of the movie
# · change_director(new_director: str) - changes the director of the movie
# · watch() - change the watched attribute to True and increase the total watched movies class attribute (if
#     the movie is not already watched)
# · __repr__() - returns "Movie name: {name}; Movie director: {director}. Total watched movies: {__watched_movies}"

#                             Example

# Test Code                                               Output

# first_movie = Movie("Inception",                        Movie name: Inception; Movie director: Me.
# "Christopher Nolan")                                    Total watched movies: 2
# second_movie = Movie("The Matrix",                      Movie name: The Matrix; Movie director: The
# "The Wachowskis")                                       Wachowskis. Total watched movies: 2
# third_movie = Movie("The Predator",                     Movie name: My Movie; Movie director: Shane
# "Shane Black")                                          Black. Total watched movies: 2
# first_movie.change_director("Me")
# third_movie.change_name("My Movie")
# first_movie.watch()
# third_movie.watch()
# first_movie.watch()
# print(first_movie)
# print(second_movie)
# print(third_movie)



class Movie:
    __watched_movies = 0

    def __init__(self,name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self,new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"



first_movie = Movie("Inception","Christopher Nolan")
second_movie = Movie("The Matrix","The Wachowskis")
third_movie = Movie("The Predator","Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
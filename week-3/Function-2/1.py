from movies import movies


def check_imdb(movie) -> bool:
    return movie["imdb"] > 5.5


def check_movie_ny_name(name: str) -> bool:
    for movie in movies:
        if movie["name"] == name:
            return movie["imdb"] > 5.5


name = input("Name of movie: \n")
print(check_movie_ny_name(name))
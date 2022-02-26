from movies import movies


def get_movies_by_category(category: str) -> []:
    sorted_movies = []

    for movie in movies:
        if movie["category"] == category:
            sorted_movies.append(movie)

    return sorted_movies


category = input("Category\n")
print(get_movies_by_category(category))
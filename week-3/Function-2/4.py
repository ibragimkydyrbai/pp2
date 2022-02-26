from movies import movies


def count_average_imdb_score(list_of_movies: []) -> float:
    sum_of_imdb_scores = 0.0

    for movie in list_of_movies:
        sum_of_imdb_scores += movie["imdb"]

    average_imdb_score = sum_of_imdb_scores/len(list_of_movies)
    return average_imdb_score


print(f"Mean imdb = {count_average_imdb_score(movies)}")


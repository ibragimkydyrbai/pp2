from movies import movies


def count_average_imdb_score_by_category(category: str) -> float:
    sum_of_imdb_scores = 0.0
    number_of_movies_belonged_to_category = 0

    for movie in movies:
        if movie["category"] == category:
            sum_of_imdb_scores += movie["imdb"]
            number_of_movies_belonged_to_category += 1

    average_imdb_score = sum_of_imdb_scores/number_of_movies_belonged_to_category
    return average_imdb_score


category = input("Category=")
print(f"Mean imdb = {count_average_imdb_score_by_category(category)}")


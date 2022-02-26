from movies import movies


def filter_movies_by_imdb_above_5_point_5() -> []:
    new_sub_list = []

    for movie in movies:
        if movie["imdb"] > 5.5:
            new_sub_list.append(movie)
    return new_sub_list


print(f"Movies, whose imdb > 5.5\n{filter_movies_by_imdb_above_5_point_5()}")
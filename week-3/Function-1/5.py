import itertools #special library


def find_permutations(initial_string: str) -> [0]:
    characters = [c for c in initial_string]
    permutations = list(itertools.permutations(characters)) #list of tuples of characters => [('', ''), ..]
    response = []
    for permutation in permutations:
        string_value_of_permutation = ""
        for character in permutation:
            string_value_of_permutation += character
        response.append(string_value_of_permutation)

    return response


s = input("Write some string:\n")
print(find_permutations(s))

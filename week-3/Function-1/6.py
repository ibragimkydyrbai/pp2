def reverse(initial_string: str) -> str:
    reverse_string = ""

    for i in range(len(initial_string)):
        reverse_string += initial_string[-1-i]
    return reverse_string


s = input("Write something:\n")
print(reverse(s))

def is_prime(number: int):
    if number == 1: return False
    for divisor in range(2, int(number/2)+1):
        if number%divisor == 0:
            return False
    return True


def filter_prime(numbers: []) -> []:
    only_primes = []
    for number in numbers:
        if is_prime(number):
            only_primes.append(number)
    return only_primes


arr = list(map(int, input("Write numbers separated by space:\n").split()))

arr = filter_prime(arr)

print(arr)

print('If you want to convert grams to ounces, enter "1"\n')
print('If you want to calculate and display the equivalent centigrade temperature, enter "2"\n')
print('If you want to get only prime numbers from your numbers list, enter "3"\n')
print('If you want to calculate the volume of the sphere taking into account its radius, enter "4"\n')
print('If you want to checks whether a word or phrase is palindrome or not, enter "5"\n')
print('If you want to play a game "Guess the number", enter "6"\n')
print('If you want to calculate number of being with 2 legs and another with 4 legs by entering their all heads and all legs, enter "7"\n')
print('If you want to print a histogram to the screen, enter "8"\n')
print('If you want to print all permutations of that string, enter "9"\n')
print('If you want to reverse words, enter "10"\n')
enter = int(input())

if enter == 1:
    g = int(input("Insert mass in grams\n"))
    def ounces(grams):
        return 28.3495231 * grams
    print(f'Ounces = {ounces(g)}')

elif enter == 2:
    def fahrenheit(c):
        return (5/9)*(c-32)
    c = int(input("Insert Celsius temperature: \n"))
    print(f'Fahrenheit temperature = {fahrenheit(c)}')

elif enter == 3:
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

elif enter == 4:
    def volume(radius: int):
        v=(4/3)*3.14*pow(radius,3)
        return v
    print('Write radius of sphere:')
    r = int(input())

    print(volume(r))

elif enter == 5:
    def is_palindrome(s: str) -> bool:
        for i in range(int(len(s)/2)):
            if s[i] != s[-1-i]:
                return False
        return True


    s = input("Write word:\n")
    if is_palindrome(s):
        print("Is Palendrom")
    else:
        print("Not palendrom")
elif enter == 6:
    import random


    def guess_a_number():
        name = input("Hello! What is your name?\n")
        print()
        number = random.randint(1, 20)
        print(f'Well, {name}, I am thinking of a number between 1 and 20.')

        number_of_trials = 1

        while True:
            guess = int(input("Take a guess.\n"))
            print()
            if guess == number:
                print(f'Good job, {name}! You guessed my number in {number_of_trials} guesses!')
                break
            else:
                number_of_trials += 1
                if guess < number:
                    print("Your guess is too low.")
                elif guess > number:
                    print("Your guess is too high.")


    guess_a_number()

elif enter == 7:
    def solve(numheads, numlegs):
        if numlegs % 2 != 0:
            return "It is impossible to solve the problem!"
    # hens+rabbits=heads  => R1             => hens+rabbits=heads   => hens=heads-rabbits
    # 2hens+4rabbits=legs => R2 -> -2R1+R2  => 2rabbits=legs-2heads => rabbits=legs/2-heads
        rabbits = numlegs/2-numheads
        hens = numheads-rabbits

        if rabbits < 0 or hens < 0:
            return "It is impossible to solve the problem!"
        return {"rabbits": rabbits, "hens": hens}


    numheads, numlegs = list(map(int, input("Insert number of heds and number of legs\n").split()))

    print(solve(numheads, numlegs))

elif enter == 8:
    print('How many histogram do you want to print:')
    def histogram(arr):
        for i in arr:
            print('*'*i)


    li = list(map(int, input().split()))

    histogram(li)

elif enter == 9:
    import itertools #special library


    def find_permutations(initial_string: str) -> []:
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

elif enter == 10:
    def reverse(initial_string: str) -> str:
        reverse_string = ""

        for i in range(len(initial_string)):
            reverse_string += initial_string[-1-i]
        return reverse_string


    s = input("Write something:\n")
    print(reverse(s))


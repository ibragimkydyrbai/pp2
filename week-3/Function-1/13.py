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
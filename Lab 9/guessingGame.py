import random


def RNG():
    output = random.randint(1, 20)
    return output


def reciever():
    while True:
        try:
            guess = int(input("Take a guess: "))
            if guess > 20 or guess < 0:
                print("Enter a number between 1-20")
            else:
                break
        except ValueError:
            print("Enter a number!")
    return guess


def checker(rngOut, guess):
    if guess > rngOut:
        print("Too high, go lower!")
        return "l"
    if guess < rngOut:
        print("Too low, reach higher!")
        return "h"
    if guess == rngOut:
        print("You got it!")
        return "win"


# rngOut = RNG()
# print(rngOut)
# guess = reciever()
# print(guess)
# checker(rngOut, guess)

while True:
    rngOut = RNG()
    print(rngOut)
    while True:
        guess = reciever()
        i = checker(rngOut, guess)
        if i == "win":
            break
    play = input("Play again? Y/N: ")
    if play == 'Y' or play == 'y':
        continue
    if play == 'N' or play == 'n':
        print("Good Bye!")
        break

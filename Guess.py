from random import randint

target = randint(1,100)

stop = False
while stop == False:
    guessed = int( input("\nGuess a number that I think (target) between 1 and 100: "))

    if guessed > target:
        print("Your number is GREATER than target.")
    elif guessed < target:
        print("Your number is LESS than target.")
    else:
        stop=True

print("\nCongrats ! You won.\n\n")


import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Guess a random number between {low} to {high} :"))
    guesses += 1

    if guess < low or guess > high:
        print(f"{guess} is out of Range\nPlease Guess between {low} to {high}")
    elif guess > number:
        print(f"Your {guess} is High!")
    elif guess < number:
        print(f"Your {guess} is too Low!")
    else:
        print(f"{guess} is correct")
        break

print(f"THis round took you {guesses} guess")





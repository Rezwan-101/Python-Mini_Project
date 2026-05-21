import random

options = ("ROCK", "PAPER", "SCISSORS")
running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:

        player = input("Enter a choice (ROCK, PAPER, SCISSORS) :").upper()

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "ROCK" and computer == "SCCISSORS":
        print("You win!")
    elif player == "PAPER" and computer == "ROCK":
        print("You win!")
    elif player == "SCISSORS" and computer == "PAPER":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play Again? (Y/N): ").upper()

    if  not play_again == "Y":
        running = False

print("Thanks For Playing!")




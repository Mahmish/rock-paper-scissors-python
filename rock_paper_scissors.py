import random

options = ("rock", "paper", "scissors")
running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    
    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    elif player == "scissors" and computer == "paper":
        print("You Win")
    else:
        print("You Lose")

        play_again = input("Play again? (y/n): ").lower() == "y"
        if not play_again == "y":
            running = False
#   if not input("Play again? (y/n): ").lower() == "y"(another way of writting upper statement)

print("Thanks for Playing")
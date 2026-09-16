import random

options = ("rock","paper","scissors")

running = True

while running : 
    playerChoice = None
    computerChoice = random.choice(options)

    while playerChoice not in options:
        playerChoice = input("enter your choice (rock,paper,scissiors) :")

    print(f"player : {playerChoice}")
    print(f"computer : {computerChoice}")


    if playerChoice == computerChoice:
        print("its a tie")
    elif playerChoice == "rock" and computerChoice == "Scissors":
        print("Player wins")
    elif playerChoice == "paper" and computerChoice == "rock":
        print("Player wins")
    elif playerChoice == "scissors" and computerChoice == "paper":
        print("Player wins")
    else :
        print("Computer wins")

    # playAgain = input("Do you want to play again (y/n) : ").lower
    # if playAgain == "n" :
    #     running = False
    # elif playAgain != "n" or playAgain != "y"  :
    #     print("Invalid")
    #     running = False

    if not input("Do you want to continue(y/n) :").lower == "y":
        running = False

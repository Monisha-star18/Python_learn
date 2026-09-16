playerChoice = input("Enter rock, paper, or scissors: ")

match playerChoice:
    case "rock":
        print("You selected Rock")

    case "paper":
        print("You selected Paper")

    case "scissors":
        print("You selected Scissors")

    case _:
        print("Invalid choice")
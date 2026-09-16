#Banking project 



def withdraw(balance):
    withdrawAmount = int (input ("Enter the amount you need to withdraw : "))

    if withdrawAmount <= 0 :
        print("Invalid amount")
        return 0;
    elif withdrawAmount > balance :
        print("Transaction failed : insufficeint balance")
        return 0;
    else :
        return withdrawAmount
    

def deposit():
    amount = int(input("Enter the amount to deposit :"))

    if amount<=0 :
        print("Invalid amount to deposit")
        return 0;
    else :
        return amount

def show_balance(balance):
    print(f"Your balance is ${balance:.3f}")

def main ():
        
    balance = 0
    is_running = True


    while is_running:
        print("Banking app running")

        print("""
                1. Check balance 
                2. Deposit
                3. Withdraw
                4. Exit
                """)
        choice = int(input("Enter the choice(1-4) : "))

        match choice:
            case 1 :
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -=withdraw(balance)
            case 4 :
                is_running = False
            case _:
                print("Invalid choice")
    print("Thank you have  a nice day !")


if __name__ == '__main__':
    main()
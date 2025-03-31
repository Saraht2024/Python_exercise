# Python Banking Program

def show_balance(balance):
    """Displays the current balance."""
    print("\n***************************")
    print(f"Your current balance is: ${balance:.2f}")
    print("***************************\n")

def deposit():
    """Handles deposits and ensures a valid input."""
    print("\n***************************")
    while True:
        try:
            amount = float(input("Enter an amount to deposit: $"))
            if amount <= 0:
                print("Invalid amount! Please enter a positive number.")
            else:
                print(f"Successfully deposited: ${amount:.2f}")
                return amount
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def withdraw(balance):
    """Handles withdrawals and ensures a valid input."""
    print("\n***************************")
    while True:
        try:
            amount = float(input("Enter an amount to withdraw: $"))
            if amount > balance:
                print("Insufficient funds! Try a smaller amount.")
            elif amount <= 0:
                print("Invalid amount! Please enter a positive number.")
            else:
                print(f"Successfully withdrew: ${amount:.2f}")
                return amount
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    """Main function to run the banking program."""
    balance = 0.0
    is_running = True

    while is_running:
        print("\n***************************")
        print("      Banking Program      ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************************\n")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("\n***************************")
            print("Invalid choice! Please enter a number between 1 and 4.")
            print("***************************\n")

    print("\n***************************")
    print(f"Final balance: ${balance:.2f}")
    print("Thank you for using our banking system! Have a great day!")
    print("***************************")

if __name__ == '__main__':  
    main()

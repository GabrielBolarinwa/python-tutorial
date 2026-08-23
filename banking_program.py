def show_balance(balance):
    print(f"Your balance is ₦{balance:,.2f}")


def deposit():
    amount = input("Enter the amount you want to deposit: ")
    while not amount.isdigit():
        print("Please enter a valid amount")
        amount = input("Enter the amount you want to deposit: ")
    amount = float(amount)
    while amount < 0:
        print("Please enter an amount greater than 0")
        amount = input("Enter the amount you want to deposit: ")
        amount = float(amount)
    return amount


def withdraw(balance):
    amount = input("Enter the amount you want to withdraw: ")
    while not amount.isdigit():
        print("Please enter a valid amount")
        amount = input("Enter the amount you want to withdraw: ")
    amount = float(amount)
    while amount < 0:
        print("Please enter an amount greater than 0")
        amount = input("Enter the amount you want to withdraw: ")
        amount = float(amount)
    if amount > balance:
        print("Insufficient funds")
        return 0
    return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid choice")

    print("Thanks for banking with us")


if __name__ == "__main__":
    main()

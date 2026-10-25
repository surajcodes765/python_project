#ATM CARD
correct_pin = "1234"
balance = 10000
attempts = 3
history = []
authenticated = False

# Stage 1: PIN check
while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        authenticated = False
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong PIN. Attempts left: {attempts}")
        else:
            print("Card blocked.")

# Stage 2, 3, & 4: Menu, Transactions, and History Extension
if authenticated:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            print(f"New balance: {int(balance)}")
            
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"New balance: {int(balance)}")
                history.append(f"Deposit {int(amount)}")
            else:
                print("Amount must be above 0.")
                
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance")
            elif amount <= 0:
                print("Amount must be above 0.")
            else:
                balance -= amount
                print(f"New balance: {int(balance)}")
                history.append(f"Withdraw {int(amount)}")
                
        elif choice == "4":
            print("Thank you!")
            if history:
                for item in history:
                    print(item)
            break
        else:
            print("Invalid choice. Please select 1-4.")

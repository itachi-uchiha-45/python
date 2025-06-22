int_correct_pin = "0045"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ") 

    if entered_pin == int_correct_pin:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempts left.")
        else:
            print("Account Locked. Too many failed attempts.")
            break


1 == "Check Balance"  
2 == "Deposit Money"  
3 == "Withdraw Money"  
4 == "Exit"  

int_balance = 1000

while True:
    print("\n==== ATM Menu ====")    
    print("1. Check Balance")    
    print("2. Deposit Money")    
    print("3. Withdraw Money")    
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your current balance is ₹{int_balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount >= 0:
            int_balance += amount
            print(f"₹{amount} deposited successfully. Your current account balance: ₹{int_balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount > 0:
            if amount <= int_balance:
                int_balance -= amount  # fixed here
                print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{int_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    elif choice == "4":
        print("Thank you for using ATM. GOODBYE!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        break
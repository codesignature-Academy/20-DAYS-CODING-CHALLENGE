from jpay import Bank

bank1 = Bank("john")

print("Welcome to Jpay online Bank")

while True:
    print("Choose an option below:")
    print("A. Deposit")
    print("B. Transfer")
    print("C. Withdraw")
    print("D. Check Balance")
    print("quit")
    
    option = input("============ ").upper()
    
    if option == "A":
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            bank1.deposit(amount)
            
    elif option == "B":
        try:
            amount = float(input("Enter amount to transfer: "))
            acct_num = input("Enter destination account number: ")
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            bank1.transfer(amount, acct_num)
            
    elif option == "C":
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            bank1.withdraw(amount)
    
    elif option == "D":
        bank1.check_balance()
        
    elif option.lower() == "quit":
        print("Exiting...")
        break
    
    else:
        print("invalid option\nTry again")
        continue
    
    
print("Thank you for banking with us...")
            
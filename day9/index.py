from mathematics import add, subtract, divide, multiply, power, get_remainder

print("Welcome to our calculator")
choice = "yes"

while choice == "yes":
    print("Choose an option below:")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Division")
    print("D. Multiplication")
    print("E. Exponentiation")
    print("F. Get Remainder")
    print("q to quit")
    
    option = input("======= ").lower()
    
    if option == "q":
        print("Exiting Calculator")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    
    if option.upper() == "A":
        print(f"The sum of {num1} and {num2} = {add(num1, num2)}")
    elif option.upper() == "B":
        print(f"The difference of {num1} and {num2} = {subtract(num1, num2)}")
    elif option.upper() == "C":
        print(f"{num1} divided by {num2} = {divide(num1, num2)}")
    elif option.upper() == "D":
        print(f"The product of {num1} and {num2} = {multiply(num1, num2)}")
    elif option.upper() == "E":
        print(f"{num1} raised to power {num2} = {power(num1, num2)}")
    elif option.upper() == "F":
        print(f"The remainder of {num1} divided by {num2} = {get_remainder(num1, num2)}")
    else:
        print("Invalid option\nTry Again")
        
    while True:
        choice = input("Do you want to continue (yes or no)? ").lower()
        
        if choice == "no" or choice == "yes":
            break
        else:
            print("Invalid choice must be (yes or no)")
            continue
        
else:
    print("'Thank you for using our calculator\nGoodBye")
        
"""
while True:
    print("yes")
else:
    print("no)
"""       
        
        
        

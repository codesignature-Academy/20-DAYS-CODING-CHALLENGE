print("Welcome to my calculator!")

choice = "yes"

while choice == "yes":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operator = input("choose an operator (+, -, *, /): ")
        
        if operator == '+':
            print(f"The sum of {num1} and {num2} = {num1 + num2}")
        elif operator == '-':
            print(f"The difference of {num1} and {num2} = {num1 - num2}")
        elif operator == '*':
            print(f"The product of {num1} and {num2} is {num1 * num2}")
        elif operator == "/":
            print(f"{num1} divided by {num2} = {num1 / num2}")
        else:
            raise ValueError("Invalid operator")
        
    except ValueError as e:
        print(f"Error == {e}")
        
    except ZeroDivisionError:
        print(f"Error == Division by zero is not allowed.")
        
    finally:
        # ask the user if they want to continue
        
        # use while loop
        
        # check the user's input
        
        # if yes == continue
        
        # elif no == break
        
        # else == invalid choice
        
        # continue
        ...
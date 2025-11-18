while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == "smart" and password == "smart@123":
        print("Access granted")
        break
    elif username == "rejoice" and password == "rejoice@123":
        print("Access granted")
        break
    else:
        print("Access Denied")
        print("Invalid Username or password\nTry again")


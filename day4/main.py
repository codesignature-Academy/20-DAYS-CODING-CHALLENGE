username = input("Enter your username: ").lower()
password = input("Enter your password: ")
"""
John is a web developer
John Is A Web Developer
"""

# and, or, not
# .lower(), .upper(), .title(), .strip(), .capitalize()

if username == "rejoice" and password == "rejoice@123":
    print("Access granted")
elif username == "input" and password == "input@123":
    print("Access granted")
elif username == "gerald" and password == "gerald@123":
    print("Access granted")
else:
    print("Access denied")
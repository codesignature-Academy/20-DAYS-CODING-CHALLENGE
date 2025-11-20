import string
import secrets


def generate_password(length, digits=True, special_chars=True):
    character = ""
    
    character = string.ascii_letters # uppercase and lowercase letters
    if digits:
        character += string.digits
    if special_chars:
        character += string.punctuation
        
    password = ''.join(secrets.choice(character) for _ in range(length)) # create a password of length {length}
    
    return password


length = int(input("Enter password length: "))
digits = input("Do you wish add digits in your password (yes or no): ")
special_chars = input("Do you wish add special characters in your password (yes or no): ")

if digits.lower() == "yes" and special_chars.lower() == "yes":
    password = generate_password(length, digits=True, special_chars=True)
elif digits.lower() == "yes" and special_chars.lower() == "no":
    password = generate_password(length, digits=True, special_chars=False)
elif digits.lower() == "no" and special_chars.lower() == "yes":
    password = generate_password(length, digits=False, special_chars=True)
else:
    password = generate_password(length, digits=False, special_chars=False)

print(f"Your password is: {password}")
    

    

    
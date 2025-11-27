"""
TASK 3 — Phone Number Validator

Create a program that:

✔ Accepts a phone number from the user

Rules:

Must be 11 digits

Must contain only numbers

Must start with 0 (like Nigerian phone numbers: 080..., 090...)

✔ Use error handling to manage:

If the user enters letters → catch ValueError

If the length is not 11 → raise your own Exception

If the first digit is not 0 → raise your own Exception

✔ Use:

try

except

else

finally
"""

try:
    phone = str(input("Enter your phone number: "))
    if phone.startswith("+"):
        _, number = phone.split('+')
        
    if not number.isdigit():
        raise ValueError("Phone Number must not contain letters or special characters")
    
    if len(number) < 11 or len(number) > 13:
        raise Exception("Phone Number must have 11-13 digits")
    
    if phone.startswith("0") or phone.startswith("+234"):
        pass
    else:
        raise Exception("Phone Number Must Start with 0")
    
    
    
except ValueError as ve:
    print(f"Error: {ve}")
    
except Exception as e:
    print(f"Error: {e}")
    
else:
    print(f"Phone number {phone} is valid")

finally:
    print("Bye Bye")
    


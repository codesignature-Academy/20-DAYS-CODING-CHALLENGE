import string
import getpass

def get_password_strength(password):
    password_score = 0
    results = []
    
    if len(password) < 8:
        results.append("Password is too short...Must have a minimum of 8 characters")
    else:
        password_score += 1
        
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special_chars = any(c in string.punctuation for c in password)
    has_digits = any(c.isdigit() for c in password)
    
    if has_lower:
        password_score += 1
    else:
        results.append("Password Does Not have lowercase letters")
        
    if has_upper:
        password_score += 1
    else:
        results.append("Password does not have uppercase letters")
    
    if has_special_chars:
        password_score += 1
    else:
        results.append("Password does not have special characters")
    
    if has_digits:
        password_score += 1
    else:
        results.append("Password does not have digits")
        
        
    if password_score >= 4:
        strength = "Strong"
    elif password_score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
        
    return strength, results


password = getpass.getpass("Enter your password: ")
strength, results = get_password_strength(password)

print(f"Password Strength === {strength}")

if results:
    print("Suggestions for improving your password:")
    for result in results:
        print(result)



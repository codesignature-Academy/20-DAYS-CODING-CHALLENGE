# eligibility checker for candidate

age = int(input("Enter your age: "))

if age > 18:
    if age < 50:
        print("Eligible")
    else:
        print("Ineligible")
else:
    print("Ineligible")
    
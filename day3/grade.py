score = float(input("Enter your score: "))
# comparison operators
"""
== , >=, <=, !=, > <
"""
if score >= 50:
    if score >= 70:
        print("Excellent")
elif score < 50:
    print("Pass")
else:
    print("Fail")
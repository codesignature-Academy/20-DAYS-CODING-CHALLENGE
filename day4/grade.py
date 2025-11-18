# 100 - 90 =  A
# 89 - 80 = B
# 79 - 70 = C
# 69 - 60 = D
# 59 - 50 = E
# else = F

score = float(input("Enter Your Score: "))

if score > 100:
    print("Score must not be more than 100")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
else:
    print("Failed")
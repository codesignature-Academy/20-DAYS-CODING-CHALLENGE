# add
def add(a,b):
    return a + b

# subtract
def subtract(a,b):
    return a - b

# divide
def divide(a, b):
    return a / b

# multiply
def multiply(a, b):
    return a * b

# get remainder
def get_remainder(a, b):
    return a % b

# Exponent
def power(a, b):
    return a ** b

# is even
def is_even(num):
    if num != 0:
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        return False

# is odd
def is_odd(num):
    if num != 0:
        if num % 2 != 0:
            return True
        else:
            return False
    else:
        return False
    
# is postive
def is_positive(num):
    if num > 0:
        return True
    else:
        return False
    
    
# factorial
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    
    return result
def main():
    
    solution = add((1,2,3,4,5))
    print(solution)
    
    solution2 = multiply((1,2,3,4,5))
    print(solution2)
    
def add(numbers):
    total = 0
    
    for num in numbers:
        total += num
    
    return total

def multiply(numbers):
    total = 1
    
    for num in numbers:
        total *= num
    
    return total
    
main()
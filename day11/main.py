# print * by the value of i == increasing by 2
for i in range(1, 14, 2):
    asterisks = '*' * i
    # align asterisks to the center 
    print(f'{asterisks:^13}')


# print * by the value of i == decreasing by 2
for i in range(11, -2, -2):
    asterisks = '*' * i
    
    # align asterisks to the center 
    print(f'{asterisks:^13}')
    
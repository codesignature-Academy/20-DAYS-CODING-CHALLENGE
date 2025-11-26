

for n in range(5):
    spaces = ' ' * (5 - n - 1)
    asterisks = '*' * (n + 1)
    
    print(asterisks + spaces + '{:>5}'.format(asterisks))
    
for n in range(5 -2, -1, -1):
    spaces = ' ' * (5 - n - 1)
    asterisks = '*' * (n + 1)
    
    # reverse order
    print(asterisks + spaces + '{:>5}'.format(asterisks))
    
  
    
    
for i in range(1, 13 + 1, 2):
    asterisks = '*' * (i)
    print(f'{asterisks:^13}')
    
for i in range(11,-2,-2):
    asterisks = '*' * (i)
    print(f'{asterisks:^13}')


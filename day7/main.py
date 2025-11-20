"""
def name_function(name):
    block of code

snake_case
camelCase
PascalCase
greet
"""
def describe_pet(animal, name):
    print(f"I have a {animal} the name is {name}")
    
# positional argument
# describe_pet("cat", "gerald")
# keyword argument
describe_pet(name="gerald", animal="cat")

# Default argument
def greet(name="helen"):
    print(f"Hello, {name}")
    
greet("John")

# Arbitrary Arguments *args and **kwargs
# *args for arguments and **kwargs for keyword arguments
def show_all_arguments(fixed, *args, **kwargs):
    print(f"Fixed arguments: {fixed}")
    print(f"Positional arguments in tuple: {args}")
    print(f"Keyword arguments in dictionary: {kwargs}")
    
show_all_arguments(1,2,3, a=4, b=5)
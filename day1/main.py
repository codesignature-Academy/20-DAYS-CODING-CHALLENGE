# composition about yourself
# print("My name is John, I am a web developer, i love rice and chicken, i speak spanish\nI am 25 years old and I live in Mexico City.")

# create variables to store user information
name = "John"
occupation = "Web Developer"
favorite_food = "Beans"
language = "Spanish"
age = 25
residence = "Mexico City"

"""
1) variable names do not start with digits or special_characters
2) variable names must not contain any special characters except the underscore(_)
Ways to name a variable:
1) snakecase === my_variable_name
2) camelcase ==== myVariableName
3) Pascalcase ==== MyVariableName
"""

# print("My name is",name,"I am a",occupation, "i love",favorite_food, "i speak", language,"\nI am ",age ,"years old and I live in ",residence)

# age = str(age)

# print("My name is " + name +" I am a " + occupation + " i love " + favorite_food + "i speak"+ language +"\nI am " + age  + "years old and I live in " + residence)


# print(f"My name is {name}, I am a {occupation}, i love {favorite_food}, i speak {language}\nI am {age} years old and I live in {residence}.")

name = input("Enter your name: ")
occupation = input("What's Your Occupation? ")
favorite_food = input("What's Your Favorite Food? ")
language = input("What Language Do You Speak? ")
age = int(input("How Old Are You? "))
residence = input("Where Do You Reside? ")
hobbies = input("What are your hobbies? ")

print()
print()
print(f"My name is {name}, I am a {occupation}, i love {favorite_food}, i speak {language}\nI am {age} years old and I live in {residence}. My hobbies are {hobbies}.")
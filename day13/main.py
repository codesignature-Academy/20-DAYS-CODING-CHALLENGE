"""
TASK  — Student Grade Lookup App

Write a program that:
Has a dictionary like:

grades = {"john": 75, "mary": 90, "paul": 68}


Prompts the user to enter a student's name

Displays the grade

Handles:

Name not found → KeyError

Blank input → ValueError (use raise)

If name exists, print the grade

Always print "Search Complete" using finally
"""
grades = {"john": 75, "mary": 90, "paul": 68}

try:
    name = input("Enter Student's name: ").strip()
    
    if name == "":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        raise ValueError("Name field must not be empty")
    
    print(f"{name}'s grade is {grades[name]}")
    
except KeyError:
    print("Error: Name does not exist")

except ValueError as ve: 
    print(f"Error: {ve}")
    
finally:
    print("Search completed")
    
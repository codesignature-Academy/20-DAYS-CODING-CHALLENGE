"""

  🔹  ======  ====== Basic While Loop Project: Number Guessing Game ======  ====== 

    🎯  ======  ====== Project Goal ======  ====== 

Let the computer choose a random number, and the user keeps guessing until they get it right.

    🧠  ======  ====== Concepts Practiced ======  ====== 

 ======  `while` loop
 ======  User input
 ======  Conditional statements
 ======  Loop termination

---

  📌  ======  ====== Project Description ======  ====== 

1. The computer picks a random number between 1 and 20.
2. The program asks the user to guess the number.
3. If the guess is wrong, it gives a hint (too high / too low).
4. The `while` loop continues until the user guesses correctly.
5. When the user gets it right, the loop stops and the program ends.

---

  📝  ======  ====== What You’ll Implement ======  ====== 

 ======  A `while True` loop (or a loop based on a condition)
 ======  `break` to stop the loop
 ======  Comparing user guesses with the secret number
 ======  Simple messages to guide the player

"""
import random

computers_choice = random.randint(1, 20)
attempts = 0

while attempts < 5:
    
    guess = int(input("Choose a number: "))
    
    if guess == computers_choice:
        print("You guessed right...")
        break
    elif guess > computers_choice:
        print("Too high")
        attempts += 1
    else:
        print("Too low")
        attempts += 1
        
    print(f"Number of attempts left == {5 - attempts}")
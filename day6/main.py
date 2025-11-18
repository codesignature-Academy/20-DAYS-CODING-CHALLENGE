"""
  🔹  ======  ====== FOR LOOP Project: Vowel Counter ======  ====== 

    🎯  ======  ====== Goal ======  ====== 

Ask the user to enter a word or sentence, and use a  ======  ====== for loop ======  ======  to count how many  ======  ====== vowels ======  ======  (a, e, i, o, u) appear.

---

   ✔️  ======  ====== What the Program Should Do ======  ====== 

1. Ask the user to type any text.
2. Convert the text to lowercase so counting is easier.
3. Use a  ======  ====== for loop ======  ======  to go through each character.
4. Check if each character is a vowel.
5. Count how many vowels appear.
6. Print the total number of vowels.

---

   🧠  ======  ====== What You Will Learn ======  ====== 

 ======  Looping through a string character by character
 ======  Using conditions inside loops
 ======  Using counters
 ======  Comparing letters and filtering characters

---

   📌  ======  ====== Example Output ======  ====== 

If the user enters:

 ======  ====== "Python is awesome" ======  ====== 

The program should detect these vowels:

 ======  ====== o, i, a, e, o, e → 6 vowels ======  ====== 

"""

text = input("Type any text: ").lower()
vowels = ('a','e','i','o','u')
vowel_count = []

for i in text:
    if i in vowels:
        vowel_count.append(i)
    else:
        continue
    
print(f"Number of vowels in your text == {len(vowel_count)}")
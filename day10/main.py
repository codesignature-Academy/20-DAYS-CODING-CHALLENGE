# palindrome checker
# hannah == reversed == hannah == is_palindrome
# man == reversed == nam == is_not_palindrome



def is_palindrome(n:list):
    palindromes = []
    non_palindromes = []
    
    for word in n:
        if word[::-1] == word:
            palindromes.append(word)
        else:
            non_palindromes.append(word)
            
    return palindromes, non_palindromes


sentence = ['hannah', 'man', 'mom', 'pot', 'dad']

palindrome, non_palindrome = is_palindrome(sentence)

if palindrome:
    print(f"Palidromes in {sentence}")
    for p in palindrome:
        print(f"=== {p}")
        
if non_palindrome:
    print(f"NonPalidromes in {sentence}")
    for n in non_palindrome:
        print(f"=== {n}")
    


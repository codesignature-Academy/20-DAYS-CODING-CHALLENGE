# global variable
count_words = {}

def words_count(sentence):
    global count_words
    
    # local variable
    words = sentence.split(" ")
    for word in words:
        if word in count_words:
            continue
        else:
            count_words[word] = words.count(word)
        
    return count_words

text = input("Enter a sentence: ")
print(words_count(text))
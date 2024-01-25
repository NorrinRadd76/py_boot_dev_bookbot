print("Hello World")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    file_contents = file_contents.lower()
    
    words = file_contents.split()
    letters = {"non_alpha": 0}
    for word in words:
        for letter in word:
            if letter.isalpha() == False:
                letters["non_alpha"] += 1
                continue
            
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    print(f"This book has {len(words)} words")
    
    non_alpha = letters.pop("non_alpha")
    print(letters)
    letters_list = list(letters)
    letters_list.sort()
    
    for letter in letters_list:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print(f"Non-Alphanumeric characters were found {non_alpha} times")
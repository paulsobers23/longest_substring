def longest_substring(word):
    letter_count = 0
    
    non_repeat_char = {}
    for letter in word:
        if letter in word:
            non_repeat_char[letter] += 1   
            letter_count += 1
        else:
            
     
  
print(longest_substring('abc'))
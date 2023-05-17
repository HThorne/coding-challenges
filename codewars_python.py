# Below are all the coding challenges I have completed on codewars.com. 
# Instructions given are in the docstrings.

def even_or_odd(number):
    """Take an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers."""
    if number % 2 == 0:  # % finds remainder, all evens should be divisible by 2 with 0 remainder
        return "Even"
    else:
        return "Odd"
    

def boolean_to_string(b):
    """Convert the given boolean value into its string representation."""
    return str(b)

    # if built in conversion were not allowed, would use if/else and return strings based on given


def digitize(n):
    """Return the digits of this number within an array in reverse order."""
    reverse_array = []
    n = str(n)     # make n a string so that it is iterable
    
    for num in n:        # iterate through each char in string n and turn into int before appending to list
        num = int(num)
        reverse_array.append(num)
        
    reverse_array = reverse_array[::-1]  # get reverse list by splicing with a negative step
        
    return reverse_array


def get_count(sentence):
    """Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces."""
    count = 0
    
    for char in sentence:
        if char in "aeiou":
            count += 1
            
    return count


def disemvowel(string_):
    """Trolls are attacking your comment section!
    A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
    Your task is to write a function that takes a string and return a new string with all vowels removed.
    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
    Note: for this kata y isn't considered a vowel."""
    for char in string_:
        if char in "aeiouAEIOU":
            string_ = string_.replace(char, "")
    return string_


def sum_mutiples(number):
    """Return the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
    Note: If the number is a multiple of both 3 and 5, only count it once."""
    count = 0
    
    if number < 0:
        return 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            count += i
            
    return count


def spin_words(sentence):
    """Return the same string, but with all five or more letter words reversed"""
    words = sentence.split()      # Make a list of words from the sentence based on where the whitespaces are
    
    for i, word in enumerate(words):  # Loop through list looking for words longer than 4 characters
        if len(word) >= 5:  
            words[i] = word[::-1]      # Reverse the word and assign to old index
            
    return " ".join(words)


def move_zeros(nums):
    """Take an array and moves all of the zeros to the end, preserving the order of the other elements."""
    i = 0         # index to search if zero 
    n = 0
    
    while n < len(nums):      # Loop the length of the list
        if nums[i] == 0:  # Search index number instead of num because index will change and miss zeros if not
            zero = nums.pop(i)
            nums.append(zero)
        else:             # if not zero move the index to search forward
            i += 1
        n += 1
        
    return nums


def pig_it(text):
    """Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched."""
    words = text.split()    # split text into list of words
    
    for i, word in enumerate(words):  # Loop through words and change/reassign at index, skip if punctuation 
        if word.isalpha():
            first_letter = word[0]
            word = word[1:]
            word += first_letter
            word += "ay"

            words[i] = word
        
    return ' '.join(words)
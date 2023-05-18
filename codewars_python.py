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


# First attempt
def make_readable(seconds):
    """Take a non-negative integer (seconds) as input.
    Returns the time in a human-readable format (HH:MM:SS)"""
    hours = (seconds // 60) // 60
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    
    # Handle if number is less than 10 needing zero in front
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    
    return f"{hours}:{minutes}:{seconds}"


# Second attempt 
def make_readable(seconds):
    """Take a non-negative integer (seconds) as input.
    Returns the time in a human-readable format (HH:MM:SS)"""
    
    return f"{seconds // 3600:02}:{(seconds // 60) % 60:02}:{seconds % 60:02}"


def rgb(r, g, b):
    """Take RGB decimal values and convert it into a hexadecimal representation being returned. 
    Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value."""
    conversion_table = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    rgb = [r, g, b]
    hexadec = ''
    
    for value in rgb:
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        hexadec += f'{conversion_table[value // 16]}{conversion_table[value % 16]}'
        
    return hexadec


def snail(snail_maps):
    """Given an array of arrays, return the array elements arranged from outermost elements to the middle element, traveling clockwise."""
    snail = []
    
    while len(snail_maps) > 0:
        if len(snail_maps) == 1:           # Account for last list
            snail.extend(snail_maps[0])
            break
        
        snail.extend(snail_maps[0])    # Add entire top list in order and then remove
        snail_maps.pop(0)
        
        for snail_map in snail_maps:      # Loop adding and removing last element in each list
            snail.append(snail_map[-1])
            snail_map.pop()
        
        snail.extend(snail_maps[-1][::-1])  # Add entire bottom list in reverse order and then remove
        snail_maps.pop()
        
        
        for snail_map in snail_maps[::-1]:  # Loop adding and removing first element in each list
            snail.append(snail_map[0])
            snail_map.pop(0)
            
    return snail


def solution(nums):
    """Take a list of integers in increasing order and returns a correctly formatted string in the range format.
    
    ex: solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
    """
    solution = []     # Using an empty list rather than an empty str to make comparison easier

    for i, num1 in enumerate(nums):
        if len(solution) > 1 and num1 <= solution[-2]:  # Continue past any numbers that are already in a range
            continue
        
        low_end = num1
        high_end = num1
        
        if i + 1 < len(nums):             # Find end of consecutive range of numbers
            for num2 in nums[i + 1:]:
                if num2 == high_end + 1:
                    high_end = num2
        
        if low_end == high_end or high_end == low_end + 1:  # This accounts for numbers outside any ranges
            solution.extend([num1, ','])
        else:
            solution.extend([low_end, '-', high_end, ","])
    
    solution.pop()       # Remove trailing comma
    
    for i, num3 in enumerate(solution):    # Convert all numeric to strings so they can be joined
        solution[i] = str(num3)

    
    return "".join(solution)


def nb_year(p0, percent, aug, p):
    """In a small town the population is p0 at the beginning of a year. 
    The population regularly increases by a percent per year and 
    moreover new inhabitants(aug) per year come to live in the town. 
    How many years does the town need to see its population greater or equal to p?"""
    years = 0
    
    while p0 < p:
        p0 = int(p0 + (p0 * (percent / 100)) + aug)
        years += 1
        
    return years
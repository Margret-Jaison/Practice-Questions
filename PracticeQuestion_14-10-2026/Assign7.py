# Question 9: String processing
# Write a function that accepts a string and returns the number of vowels, consonants, digits, and spaces.
# Example input: "Python 123"
# Expected counts:
# ●	Vowels: 1
# ●	Consonants: 5
# ●	Digits: 3
# ●	Spaces: 1

def charcheck(text):
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0

    for char in text:
        if char in 'aeiouAEIOU':
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    return vowels, consonants, digits, spaces

print(charcheck("Python 123"))
    
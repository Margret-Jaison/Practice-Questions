# 2. Character frequency 
# Given the string 'programming', count the frequency of every character using a dictionary.

string = 'programming'
frequency = {}
for char in string:
  if char in frequency:
    frequency[char]+=1
  else:
    frequency[char]=1

print("Character frequency in the string is:", frequency)
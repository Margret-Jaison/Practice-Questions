# Question 7: Lambda function
# Given the list:
# numbers = [12, 5, 18, 7, 24, 9, 30]
# Use lambda function to obtain all numbers multiplied by 3.
numbers=[12, 5, 18, 7, 24, 9, 30]
multiplied_numbers=lambda x: x*3
print(list(map(multiplied_numbers,numbers)))
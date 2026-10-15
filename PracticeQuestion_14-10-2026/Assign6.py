# Question 8: Recursion
# Write a recursive function to calculate the factorial of a number.
# Example: factorial(5) returns 120.

def factorial(n):
  if(n==0 or n==1):
     return 1
  else:
     fact=n*factorial(n-1)
  return fact

print(factorial(5))


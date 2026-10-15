# Question 6: Function with return value
# Write a function calculate_bill(price, quantity) that returns the total bill amount. If the bill exceeds ₹2,000, apply a 10% discount.
# Example: calculate_bill(500, 5) should return 2250.0.

def calculate_bill(price,quantity):
  totalPrice=price*quantity
  if totalPrice>2000:
    discount =totalPrice*0.1
    totalPrice=totalPrice-discount
  return totalPrice
print(calculate_bill(500,5))
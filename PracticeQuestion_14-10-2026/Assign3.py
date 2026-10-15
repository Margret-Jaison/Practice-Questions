# 3. Student marks analysis · 
# Store three students and their marks in a dictionary. Print each student's result as Pass (marks >= 40) or Fail.
marks={
    'Alice': 85,
    'Mary': 35,
    'Annie': 55}
for student, mark in marks.items():

      if mark >= 40:
        result = 'Pass'
      else:
        result = 'Fail'
      print(f"{student}: {result}")
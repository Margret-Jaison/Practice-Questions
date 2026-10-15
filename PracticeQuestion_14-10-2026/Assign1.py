#1. First largest number · 
#Given [12, 5, 8, 20, 15], find the first largest number

List=[12, 5, 8, 20, 15]
max=List[0]
for i in List:
   if(i>max):
        max=i
print("The first largest number is:", max)
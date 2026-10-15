# Create employees.csv with the columns id, name, and salary.
import csv
with open(r"C:\Users\JOSEP\Documents\PracticeAssignments\employees.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","salary"])
    writer.writerow([1,"John",50000])
    writer.writerow([2,"Alice",60000])
    writer.writerow([3,"Bob",55000])
    writer.writerow([4,"Eve",70000])
    writer.writerow([5,"Charlie",65000])
print("employees.csv file created successfully.")    
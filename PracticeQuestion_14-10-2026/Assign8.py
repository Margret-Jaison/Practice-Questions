# Question 10: Text file
# Create a file named notes.txt and write five lines into it. Then:
# ●	Read and print the complete file.

file=open("notes.txt","r")
content=file.read()
print(content)
file.close()

# ●	Print only the third line.
file=open("notes.txt","r")
lines=file.readlines()
print("\n"+lines[2])
file.close()



# ●	Append one more line without deleting existing content.
with open(r"C:\Users\JOSEP\Documents\PracticeAssignments\notes.txt","a")as file:
    file.write("\nThis is the sixth line.")
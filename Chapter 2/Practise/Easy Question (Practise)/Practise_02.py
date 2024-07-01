# Given the dictionary student = {"name": "Bob", "grade": "A", "subject": "Math"}, write a loop to print each key-value pair.
student = {
    "name": "Bob",
    "grade":"A",
    "subject": "Math"
}
for i,x in student.items():
    print(str(i),":",str(x))
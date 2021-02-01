import pickle
name = input("Enter the name of student :")
file = open("student.dat","rb")
data = pickle.load(file)
file.close()
found = 0
lst = []
for d in data :
    n = d['name']
    if n == name:
        found = 1
        roll = d['roll']
        break
if found == 1:
    print(name,"found at roll number ",roll)
else:
    print("Student not found")
marks =[30,50,42,89,65,35,46,2,8]

#traversing from left to right
for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])

#traversing from right to left
for mark in reversed(marks):
    print(mark)

for mark in marks[::-1]:
    print(mark)

for i in range (len(marks)-1, -1, -1):
    print(marks[i])
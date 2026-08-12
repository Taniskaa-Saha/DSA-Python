marks = [88,90,66,45,63,78,92,55,80,70]

#add element to the end O(1)
marks.append(100)
print(marks)

#add element to specific position O(n)
marks.insert(3, 100)
print(marks)

#removes the last element O(1)
marks.pop()
print (marks)

#removes the element at specific position O(n)
marks.pop(0)
print(marks)

#also this way remove elements
marks.remove(55)
print(marks)

del marks[2] #delete element at index 2
print (marks)

#Slicing
print(marks[2:5])  # prints elements from index 2 to 4
print(marks[:5])   # prints elements from index 0 to 4
print (marks[5:])   # prints elements from index 5 to the end
print(marks[-3:])  # prints last 3 elements
print(marks[:-3])  # prints all elements except the last 3
print(marks[::2])  # prints every second element 

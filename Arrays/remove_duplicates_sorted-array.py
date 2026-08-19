def remove(names):
    left = 0
    for right in range(1, len(names)):
        if names[right] != names[left]:
            left += 1
            names[left] = names[right]
    return left + 1

names = ["mick","diya","jiya","jiya","aman","mick"]
names.sort()
count = remove(names)
print(names[:count])
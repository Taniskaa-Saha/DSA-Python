arr = [3, 2, 7, 1, 6]

prefix = [0]

for x in arr:
    prefix.append(prefix[-1] + x)

print(prefix)
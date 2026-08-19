def median(num1, num2):
    m = len(num1)
    n =len(num2)
    merged = num1 + num2
    merged.sort()

    if (m+n) % 2 == 1:
        return merged[(m+n) // 2]
    else:
        return (merged[(m+n) // 2 - 1] + merged[(m+n) // 2]) / 2

num1 = [1,3,5,6]
num2 = [2,4,7,8]

median_value = median(num1, num2)
print("The median of the two sorted arrays is:", median_value)
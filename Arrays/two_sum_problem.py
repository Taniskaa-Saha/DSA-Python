def find_two_numbers(num, target):
    left = 0
    right = len(num) - 1

    while left < right:
        total = num[left] + num[right]
        if total == target:
            return [num[left], num[right]]
        elif total > target:
            right = right-1
        else:
            left = left+1
    return []
    
num = [1,3,5,6,8,11]
print (find_two_numbers(num, 19))
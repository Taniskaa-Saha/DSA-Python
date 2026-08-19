def sliding_window(x, size):
    total = sum(x[0:size])
    best_total = total

    print(f"Window:{x[0:size]} = {total}")

    for i in range(size, len(x)):
        left = x[i- size]
        right =x[i]

        total = total - left + right
        window = x[i-size+1:i+1]
        print(f"Window:{window} = {total}")

        if total>best_total:
            best_total = total
    return best_total

x= [1,5,9,10,6,3,4,7,2,8]
answer = sliding_window(x, 3)
print("Best total:",answer)

#palindrome
n=int(input())
num =n
p =0
while num>0:
    d = num%10
    p=p*10+d
    num//=10
if n==p:
    print("YES")
else:
    print("NO")
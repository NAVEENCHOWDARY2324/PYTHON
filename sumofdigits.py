n = int(input())
add = 0
while (n>0):
    add = add + (n%10)
    n = int(n/10)
print(add)

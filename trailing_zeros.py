n = int(input())

res = 0
while n != 0:
    res += n//5
    n = n//5

print(res)
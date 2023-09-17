def miss(l):
    n = len(l) + 1

    # print((n*(n+1))//2, sum(l))
    return (n*(n+1))//2 - sum(l)

n = int(input())
l = list(map(int, input().split()))

print(miss(l))
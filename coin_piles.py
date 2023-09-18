def isint(a):
    return int(a) == a

def coin_piles(s1, s2):
    # solving equations
    # (s1, s2) - y1(1, 2) - y2(2, 1) = (0, 0)
    # check if solutions are valid
    y1 = (2*s2 - s1)/3
    y2 = (2*s1 - s2)/3

    # print("y1, y2", y1, y2)
    if y1 < 0 or y2 < 0:
        return "NO"
    
    if not isint(y1) or not isint(y2):
        return "NO"

    return "YES"

n = int(input())

for _ in range(n):
    s1, s2 = list(map(int, input().split()))
    print(coin_piles(s1, s2))
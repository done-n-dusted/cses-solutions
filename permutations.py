n = int(input())

def perm(n):
    if n == 1:
        return 1
    
    l = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(i)
        
    for i in range(1, n+1):
        if i % 2 == 1:
            if l != [] and abs(l[-1] - i) > 1:
                l.append(i)
            else:
                return "NO SOLUTION"
    s = ""
    for x in l:
        s += str(x) + " "

    return s

print(perm(n))
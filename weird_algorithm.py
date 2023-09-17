def weird_algo(n):
    res = []
    # if n == 1:

    while n != 1:
        res.append(n)

        if n%2 == 1:
            n = n*3 + 1
        else:
            n = n//2
        
   
    res.append(1)
    
    return res

n = int(input())
out = weird_algo(n)
for x in out:
    print(x, end=" ")
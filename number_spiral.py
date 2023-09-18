t = int(input())

def get_from(y, x):
    # mx = max(x, y)

    if y > x:
        if y%2 == 0:
           return y**2 - x + 1
        else:
            return (y-1)**2 + x
    
    else:
       if x%2 == 1:
           return x**2 - y + 1
       else:
           return (x-1)**2 + y

for _ in range(t):
    y, x = list(map(int, input().split()))
    print(get_from(y, x))
MOD = 10**9 + 7

def two_power(x):
    if x == 1:
        return 2
    
    if x == 0:
        return 1
    
    if x % 2 == 1:
        return (2*two_power(x-1))%MOD

    return ((two_power(x//2)%MOD)*(two_power(x//2)%MOD))%MOD

n = int(input())

print(two_power(n))


s = input()

def reorder(s):
    mp = {}
    for c in s:
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1
    
    # print("before",mp)
    no_odds = 0
    that_odd = ''
    for k, v in mp.items():
        if v % 2 == 1:
            no_odds += 1
            that_odd = k
            mp[k] -= 1
        if no_odds > 1:
            return "NO SOLUTION"
    # if that_odd != '':
        # del(mp[that_odd])

    res = that_odd
    # print("after", mp)
    for k, v in mp.items():
        temp = v//2
        res = k*temp + res + k*temp
    
    return res

print(reorder(s))
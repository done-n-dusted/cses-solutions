def rep(s):
    n = len(s)
    mp = {'A':0, 'G':0, 'T':0, 'C':0}
    mp[s[0]] += 1

    ct = 1
    for i in range(1, n):

        if s[i] == s[i-1]:
            ct += 1
            mp[s[i]] = max(mp[s[i]], ct)
        
        else:
            ct = 1
    
    mx = -1

    for _, v in mp.items():
        mx = max(mx, v)

    return mx


s = input()

print(rep(s))
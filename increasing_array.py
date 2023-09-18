n = int(input())
arr = list(map(int, input().split()))

def changes(arr, n):
    res = 0
    # cpare = arr[0]
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            res += arr[i-1] - arr[i]
            arr[i] = arr[i-1]
        # else:
            # cpare = arr[i]
    
    return res

print(process(arr, n))
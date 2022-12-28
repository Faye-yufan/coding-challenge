# Array Generator
### not right for 627
def arrayGenerator(arr, l, r):
    brr, cur = [], 0
    diff = 0
    
    for num in arr:
        cur = max(l, num) + diff
        if cur > r:
            return [-1]
        brr.append(cur)
        diff += 1
    return brr
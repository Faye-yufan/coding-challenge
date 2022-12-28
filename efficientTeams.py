## 10. Efficient Teams

from collections import Counter
def efficientTeams(nums):
    n = len(nums)

    total = sum(nums)
    if n % 2 or total % (n // 2) :
        return -1

    target = total // (n // 2)
    freqMap = Counter(nums)

    res = 0
    for num in nums :
        if freqMap[num] <= 0 :   # already taken 
            continue
        req = target - num
        if freqMap[req] <= 0 :  # is unable to make pair of current num ?
            return -1
        res += num * req         # count res
        freqMap[num] -= 1      # dec freq of pair nums by 1
        freqMap[req] -= 1
    return res
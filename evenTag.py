## Even Tag

### one pass, 把所有正数加起来，并记录绝对值最小的奇数，
### 如果结果为even，直接返回
### 如果结果为odd，减去这个绝对值最小的奇数。

def evenTag(value):
    absMinOdd = float('inf')
    curSum = 0
    for val in value:
        if val % 2 != 0:
            absMinOdd = min(absMinOdd, abs(val))
        if val > 0:
            curSum += val
    if curSum % 2 == 0:
        return curSum
    return curSum - absMinOdd
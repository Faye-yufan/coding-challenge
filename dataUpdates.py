# Data Updates
# brute force方法是建立count[n]遍历updates每个区间内的每个数，然后count ++  
# 优化就是，我们只需要标记left and right+1 boundary of update，到count数组，  
# 用一个公共变量cnt去计算需要改变符号的次数, 也就是 (-1) 的cnt次方，再乘以data就可以

def getFinalData(data, updates):
    count = [0] * len(data)
    for update in updates:
        l, r = update[0], update[1]
        for j in range(l-1, r):
            count[j] += 1
    finalData = data
    for i in range(len(finalData)):
        finalData[i] = data[i] * ((-1) ** count[i])
    return finalData
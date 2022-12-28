## 2. Binary Game
# 这题要判断组成good string的数目，看似复杂，其实很简单。  
# 一个good string起始只能是连续one_group个1或者zero_group个0，然后基于此再追加连续one_group个1或者zero_group个0。  
# 我们有最优子结构，无后效性，所以可以用dp。  
```python
dp = [0] * (maxlength + 1)  
dp += dp[i-onegroup]  
dp += dp[i-zerogroup]  
return sum(dp[min_length:]) % ...  
```
# 注意dp如何初始化

def binaryGame(min_length, max_length, one_group, zero_group):
    dp = [0] * (max_length + 1)
#     dp[0: min_length] = [1] * min_length
    dp[0] = 1
    
    for j in range(1, max_length + 1):
        if zero_group <= j:
            dp[j] += dp[j - zero_group]
        if one_group <= j:
            dp[j] += dp[j - one_group]
    print(dp)
    return sum(dp[min_length:]) % (10**9+7)
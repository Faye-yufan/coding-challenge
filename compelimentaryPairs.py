## Compelimentary pairs
# # words = []
# for word in words:
#     # 字符串转换为integer便于位运算
#     bitmask = 0
#     for c in word:
#         bitmask ^= (1 << (ord(c) - ord('a'))
        
#     # check bitmask 是否在hash_map（key: bitmask, value: count)中
#     # 对于26位来说各异或一次，并判断是否在hash_map中
#     # 如果在就加上对应count的数目到result中

from collections import defaultdict
def pairs(words):
    ans = 0
    bitmaskCnt = defaultdict(lambda: 0)
    for word in words:
        bitmask = 0
        for c in word:
            bitmask ^= (1 << (ord(c) - ord('a')))
        ans += bitmaskCnt[bitmask]
        bitmaskCnt[bitmask] += 1
    
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            newBitmask = bitmask
            newBitmask ^= (1 << (ord(letter) - ord('a')))
            if newBitmask in bitmaskCnt:
                ans += bitmaskCnt[newBitmask]
    return ans
    
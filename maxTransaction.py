## Bank Transaction
# 我们想交易最多，那就是在可允许的范围内把负交易都算进去。
# 所以就gready就加所有交易，并把负交易放入最小堆中， 当你发现自己交易额度为负时，就最小堆弹出，把这部分交易再补进去，这样就可以损失最小。

import heapq
def maxTransaction(transaction):
    balance, count = 0, 0
    pq = [] # A minheap is simulated using positive values
    for t in transaction:
        balance += t
        if t < 0:
            heapq.heappush(pq, t)
        print(pq)
        if balance < 0 and pq:
            balance -= heapq.heappop(pq)
            count += 1
        
    return len(transaction) - count
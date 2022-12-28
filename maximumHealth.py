# Minimum Health
### 求第k大，并且不断增加数目，所以就用最小堆，堆的size就是k，堆顶就是每层要打的人

def getMinHealth(initial_players, new_players, rank):
    pq = initial_players[:rank]
    heapq.heapify(pq)
    for ip in initial_players[rank:]:
        if pq[0] <= ip:
            heapq.heappop(pq)
            heapq.heappush(pq, ip)
    health = 0
    
    for np in new_players:
        if pq[0] <= np: # <= or =  ??
            health += heapq.heappop(pq)
            heapq.heappush(pq, np)
    health += pq[0]
    return health
# Finding integers
def findIntegers(arr, k):
    pq = arr[:k]
    ans = []
    heapq.heapify(pq)
    
    for num in arr[k:]:
        ans.append(pq[0])
        if pq[0] <= num: # <= or =  ??
            heapq.heappop(pq)
            heapq.heappush(pq, num)
    ans.append(pq[0])
    return ans
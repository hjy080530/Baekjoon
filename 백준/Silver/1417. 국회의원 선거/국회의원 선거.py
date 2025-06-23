import heapq

def solve():
    n = int(input())
    votes = []
    
    for i in range(n):
        votes.append(int(input()))
   
    if n == 1:
        return 0
    
    dasom_votes = votes[0]
    other_votes = votes[1:]
    
    max_heap = [-vote for vote in other_votes]
    heapq.heapify(max_heap)
    
    bribed = 0 
    while max_heap and dasom_votes <= -max_heap[0]:
        max_votes = -heapq.heappop(max_heap)
        max_votes -= 1
        dasom_votes += 1
        bribed += 1
        
        if max_votes > 0:
            heapq.heappush(max_heap, -max_votes)
    
    return bribed

print(solve())
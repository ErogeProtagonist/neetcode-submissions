class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -1 * i)
        
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if y < x:
                heapq.heappush(max_heap,-1*(x-y))
        if not max_heap:
            return 0
        res = max_heap[0] * -1
        return res

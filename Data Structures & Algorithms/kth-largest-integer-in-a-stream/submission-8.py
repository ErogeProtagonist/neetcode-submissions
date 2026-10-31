import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        stream = nums
        self.size = len(nums)
        heapq.heapify(stream)
        self.stream = stream
    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        self.size += 1
        temp = []
        for _ in range(self.size - self.k):
            temp.append(heapq.heappop(self.stream))
        min = self.stream[0]
        for _ in temp:
            heapq.heappush(self.stream, _)
        
        return min

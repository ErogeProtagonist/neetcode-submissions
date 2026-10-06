class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def minpos(total, h):
            print(f"The average is: {math.ceil(total / h)}")
            return math.ceil(total / h)
        def hours(n, piles, h):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / n)
            return hours
        
        max = 0
        total = 0
        for i in piles:
            if i > max:
                max = i
            total += i
        
        if h == len(piles):
            return max


        if h > len(piles):
            min_spd = minpos(total, h)
            low = min_spd
            high = max
            last_known = 0
            while low <= high:
                mid = (low + high) // 2
                print(f"mid is: {mid}")
                if (h - hours(mid, piles, h)) >= 0:
                    high = mid - 1
                    last_known = mid
                elif (h - hours(mid, piles, h)) < 0:
                    low = mid + 1
                else:
                    print("Answer")
                    return mid
                print(f"low: {low}, high: {high}")
            print("answer: ")
            return last_known

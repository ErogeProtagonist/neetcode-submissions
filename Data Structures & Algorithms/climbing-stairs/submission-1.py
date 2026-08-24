class Solution:
    def climbStairs(self, n: int) -> int:
        # You are either 1 step away from n or 2 steps away from n
        total = [0, 0]   # [how many ways if 1 step away, how many ways if 2 steps away]
        count = 2
        # n = 2
        total[0] = 1
        total[1] = 1
        answer = sum(total)
        if n <= 2:
            return n
        # n = 3
        # [2, 1]
        while count < n:
            total[1] = total[0]
            total[0] = answer
            answer = sum(total)
            count += 1
        
        return answer
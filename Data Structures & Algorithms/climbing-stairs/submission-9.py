class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 2
        b = 1
        for i in range(3, n+ 1): #[2, 1]  # [3, 2]
            total = a + b
            b = a
            a = total
        
        return total
        
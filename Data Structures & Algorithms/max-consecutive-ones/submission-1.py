class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_consecutive = [0]
        for i in nums:
            if i == 0:
                max_consecutive.append(count)
                count = 0
            else:
                count = count + i
        max_consecutive.append(count)
        return max(max_consecutive)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def track(idx, target):
            nonlocal res
            if target == 0:
                res.append(curr.copy())
                return
            if target < 0:
                return
            if idx > len(nums) - 1:
                return
            curr.append(nums[idx])
            track(idx, target - nums[idx])
            
            curr.pop()
            track(idx + 1, target)
        track(0, target)
        return res
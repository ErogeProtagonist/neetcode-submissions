class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def belt(curr, idx):
            nonlocal res
            if idx == (len(nums)):
                res.append(curr)
                return
            
            belt(curr + [nums[idx]], idx + 1)
            belt(curr,  idx + 1)

        belt([], 0)
        return res
        
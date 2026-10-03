class Solution:
    def search(self, nums: List[int], target: int) -> int:     
        l, r = 0, len(nums) - 1
        
        # the loop continues whilst the gap between l and r is at least 1 element:
        while l <= r:
            mid = (l + r) // 2
            
            if target > nums[mid]: # Search right half
                l = mid + 1
            elif target < nums[mid]: # Search left half
                r = mid - 1
            else:
                return mid
            print('target: ', target, [i for i in range(l, r + 1)])
        return -1 # Target not found
        
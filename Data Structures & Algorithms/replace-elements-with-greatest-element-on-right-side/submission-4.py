class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        z = self.greatestidx(arr, 0)
        for i in range(len(arr)):
            if i < z:
                arr[i] = arr[z]
            else:
                z = self.greatestidx(arr, i)
                arr[i] = arr[z]
        arr[len(arr)-1] = -1
        return arr
    
    def greatestidx(self, arr, v):
        greatest_idx = len(arr) - 1
        for i in range(len(arr)-1, v, -1):
            if arr[greatest_idx] < arr[i]:
                greatest_idx = i
    
        return greatest_idx
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def select(matrix):
            ml = 0
            mr = len(matrix) - 1
            while ml <= mr:
                mmid = (ml + mr) // 2
                
                if target < matrix[mmid][0]:
                    mr = mmid - 1

                elif target > matrix [mmid][-1]:
                    ml = mmid + 1

                else:
                    return matrix[mmid]
            return -1
        
        matrix2 = select(matrix)
        if matrix2 == -1:
            return False
        l, r = 0, len(matrix2) - 1
            
            # the loop continues whilst the gap between l and r is at least 1 element:

        while l <= r:
            mid = (l + r) // 2
                
            if target > matrix2[mid]: # Search right half
                    l = mid + 1
            elif target < matrix2[mid]: # Search left half
                    r = mid - 1
            else:
                return True
            print('target: ', target, [i for i in range(l, r + 1)])
        return False # Target not found
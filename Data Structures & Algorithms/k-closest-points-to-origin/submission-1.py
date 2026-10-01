class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(coordinate):
            return coordinate[0]**2 + coordinate[1]**2
    
        def quickSelect(s, e):
            if e - s + 1 <= 1:
                return
            
            
            pivot = dist(points[e])
            left = s
            for i in range(s, e):
                if dist(points[i]) < pivot:
                    points[i], points[left] = points[left], points[i]
                    left += 1
            
            points[e], points[left] = points[left], points[e]
            
            if left > k:
                quickSelect(0, left - 1)
            if left < k:
                quickSelect(left+1, e)
            if left == k:
                return
        
        quickSelect(0, len(points) - 1)
        return points[:k]
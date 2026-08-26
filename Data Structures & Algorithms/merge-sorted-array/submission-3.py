class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1         # Last element in valid nums1
        j = n - 1         # Last element in nums2
        k = m + n - 1     # Last index in nums1 array
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        # If nums2 still has leftover elements, fill them in. Nums 1 is already sorted from the back
        # (If nums1 has leftovers, they are already in their correct sorted slots)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         # Ensure that nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition positions
            Px = (low + high) // 2
            Py = (m + n + 1) // 2 - Px
            
            # Elements on the left and right of the partition
            x1 = float('-inf') if Px == 0 else nums1[Px - 1]
            x3 = float('inf') if Px == m else nums1[Px]
            
            x2 = float('-inf') if Py == 0 else nums2[Py - 1]
            x4 = float('inf') if Py == n else nums2[Py]
            
            # Check if we found the correct partition
            if x1 <= x4 and x2 <= x3:
                # If the combined length is even, return the average of the middle two elements
                if (m + n) % 2 == 0:
                    return (max(x1, x2) + min(x3, x4)) / 2.0
                # If the combined length is odd, return the middle element
                else:
                    return max(x1, x2)
            # Adjust the binary search range
            elif x1 > x4:
                high = Px - 1
            else:
                low = Px + 1
        
        # If the arrays cannot be partitioned correctly, return an error (though in theory, it should not happen)
        return -1
        
        
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        M = int(1e9 + 7)
        n = len(arr)
        
        count = 0
        odd = 0
        even = 1
        total_sum = 0
        
        for num in arr:
            total_sum += num
            
            if total_sum % 2 == 0:  # odd + even = odd
                count = (count + odd) % M
                even += 1
            else:  # even + odd = odd
                count = (count + even) % M
                odd += 1
        
        return count

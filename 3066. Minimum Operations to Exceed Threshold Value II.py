class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert nums into a min-heap (O(n))
        count = 0
        
        while nums and nums[0] < k:
            smallest = heapq.heappop(nums)  # Extract min element
            second_smallest = heapq.heappop(nums)  # Extract second min element
            
            heapq.heappush(nums, smallest * 2 + second_smallest)  # Push new value
            count += 1
        
        return count
        
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n  # Initialize the result array with 1s
        
        # Forward pass: Calculate the prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # Backward pass: Calculate the suffix products and multiply with prefix
        suffix = 1
        for i in range(n - 2, -1, -1):  # Iterate from n-2 down to 0
            suffix *= nums[i + 1]
            ans[i] *= suffix
        
        return ans
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            n = len(nums)
            ans = []
            
            for i in range(1 << n):  # Loop over 2^n combinations
                subset = []
                for j in range(n):
                    if (1 << j) & i:  # Check if the j-th bit in i is set
                        subset.append(nums[j])
                ans.append(subset)
            
            return ans

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)  # Step 1: Use a set for O(1) lookups 
        longest_streak = 0

        # Step 2: Iterate through the set
        for num in nums_set:
            # Only start a sequence if num-1 is not present
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Step 3: Continue the sequence by checking num+1 in set
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # Step 4: Update longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
        
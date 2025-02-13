class Solution:
    def get_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        mp = [0] * 82  # Since max digit sum is 81

        for num in nums:
            digit_sum = self.get_digit_sum(num)

            if mp[digit_sum] > 0:
                result = max(result, num + mp[digit_sum])

            mp[digit_sum] = max(mp[digit_sum], num)

        return result

        
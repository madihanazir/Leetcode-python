class Solution:
    def reverseBits(self, n: int) -> int:
        ans= bin(n)[2:].zfill(32)[::-1]

        return int(ans,2)


        
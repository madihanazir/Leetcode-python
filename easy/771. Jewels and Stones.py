class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = Counter(stones)
        jewels_count = 0
        for stone in stone_count:
            if stone in jewels:
                jewels_count += stone_count[stone]
        return jewels_count
        

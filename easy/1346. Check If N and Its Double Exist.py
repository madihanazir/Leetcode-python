class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
    
        for num in arr:
            # Check if the current number is double of any seen number
            # or if half of the current number exists in the seen set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the seen set
            seen.add(num)
        
        return False
          


        
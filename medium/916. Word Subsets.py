class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        # Calculate the maximum frequency required for each character in words2
        max_freq = {}
        for word in words2:
            for char in word:
                max_freq[char] = max(max_freq.get(char, 0), word.count(char))
        
        # Check each word in words1
        for word in words1:
            for char, count in max_freq.items():
                # If the word doesn't have enough occurrences of a required character, skip it
                if word.count(char) < count:
                    break
            else:
                # If all characters satisfy the condition, add the word to the result
                ans.append(word)
        
        return ans
        
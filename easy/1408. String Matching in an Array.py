class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans = set()

        # Check each word against all longer words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.add(words[i])  # Use a set to avoid duplicates
                    break  # No need to check further if a match is found
        
        return list(ans)
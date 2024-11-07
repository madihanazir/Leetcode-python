class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        # Alternate between characters of word1 and word2
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append any remaining characters from word1 or word2
        merged.append(word1[i:])
        merged.append(word2[j:])

        return ''.join(merged)

        
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        n = len(part)

        for ch in s:
            result.append(ch)

            if len(result) >= n and "".join(result[-n:]) == part:
                del result[-n:]  # Remove the last 'n' characters

        return "".join(result)
        
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
            s=list(s)
            goal=list(goal)
            
            for i in range(len(s)):

                char=s.pop(0)
                s.append(char)
                if s == goal:
                    return True

            return False
        
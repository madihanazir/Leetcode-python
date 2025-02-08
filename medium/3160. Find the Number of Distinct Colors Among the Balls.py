class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    
            n = len(queries)
            result = [0] * n
            
            colormp = {}  # color -> count
            ballmp = {}   # ball -> color
            
            for i in range(n):
                ball, color = queries[i]
                
                if ball in ballmp:  # already colored ball
                    prev_color = ballmp[ball]
                    colormp[prev_color] -= 1
                    
                    if colormp[prev_color] == 0:
                        del colormp[prev_color]
                
                ballmp[ball] = color
                colormp[color] = colormp.get(color, 0) + 1
                
                result[i] = len(colormp)
            
            return result

class Solution:
    def maxArea(self, height: List[int]) -> int:
            max_vol=0
            i= 0
            heights=0
            j=len(height)-1
            while i<j:
                if height[i]<height[j]:
                    h= height[i]
                else:
                    h=height[j]

                width= j-i

                vol= width*h

                if height[i]<height[j]:
                    i+=1
                else:
                    j-=1
                
                if vol> max_vol:
                    max_vol=vol
                    
                    
            return max_vol

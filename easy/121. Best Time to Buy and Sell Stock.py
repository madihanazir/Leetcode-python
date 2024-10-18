class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       

        l,r=0,1
        max_prof = 0
        while (r < len(prices)):
            
            diff = prices[r] - prices[l]
            
            if diff < 0:
                l+=1
                r+=1
            elif diff > max_prof:
                max_prof = diff
                r +=1
        print(max_prof)
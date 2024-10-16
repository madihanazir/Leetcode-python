class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        ans= [0]* len(temperatures)

      
        for i in range(len(temperatures)-1,-1,-1):
        
            while(stk and temperatures[i]>=temperatures[stk[-1]]):
                stk.pop()
            if stk:
                ans[i]=stk[-1]-i
            stk.append(i)
        return ans

        
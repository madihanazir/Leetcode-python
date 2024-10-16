class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''''list1=[]
        answer=[]
        for i in range(1,len(strs)):
            if sorted(strs[0])==sorted(strs[i]):
                list1.append(strs[0])
                list1.append(strs[i])
                strs.pop(0)
                strs.pop(i-1)
                answer.append(list1)
                list1=[]
        if strs:
            answer.append(strs)
        return answer'''
        list1=[]
        ans = []

        i=len(strs)-1
        #print(i)
        while(len(strs) > 0):
            if (i == -1):
                ans.append(list1)
                list1=[]
                i = len(strs)-1
                

            elif sorted(strs[i]) == sorted(strs[0]):
                list1.append(strs[i])
                strs.pop(i)
                i -= 1
            else:
                i -= 1


            '''elif (i == 0)and (len(strs) == 0):
                break'''


        if list1:
            ans.append(list1)
        return ans

            


        
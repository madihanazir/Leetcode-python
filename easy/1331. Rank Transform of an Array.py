class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cop=arr.copy()
        cop.sort()
        HM = dict()
        new = []
        rank= 1
        for i in range(len(cop)):
            if cop[i] not in HM:
                HM[cop[i]] = rank
                rank+=1
            
        

        for i in range(len(arr)):
            new.append(HM[arr[i]])
            

        return new






        

            
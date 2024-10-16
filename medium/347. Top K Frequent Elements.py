class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        du = dict()

        for key in nums:
            if key not in du:
                du[key] = 1
            else:
                du[key] += 1


        max_freq=max(du.values())

        b_list = [[] for i in range(max_freq+1)] #[] [] []

        for key , count in du.items():
            b_list[count].append(key)
            
        f_list = list(chain(*b_list))
        
        f = []

        for i in range(-1,(-k-1),-1):
            f.append(f_list[i])
        
        return f

        
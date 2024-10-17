class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
          #i=0
        #s=i+1
        nums.sort()
        #e=len(nums)-1
        #list1=[]
        ans=[]
        for i in range(len(nums)):
            s = i + 1
            e = len(nums) - 1

            if i>0 and nums[i]==nums[i-1]:
                continue
            while(s<e):
                target= nums[i]+nums[s]+nums[e]
                if(target>0):
                    e-=1
                elif(target<0):
                    s+=1
                   
                else:
                    ans.append([nums[i],nums[s],nums[e]])
                    while s < e and nums[s] == nums[s + 1]:
                        s += 1
                    
                    # Move the `e` pointer to the next different element
                    while s < e and nums[e] == nums[e - 1]:
                        e -= 1
                    
                    # After finding the triplet, move both pointers inward
                    s += 1
                    e -= 1
        return ans

        
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_c= defaultdict(int)
     

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product= nums[i] * nums[j]
           
                prod_c[product] += 1
        res= 0
        for c in prod_c.values():
            res += 8*(c* (c-1))//2
        return res

        
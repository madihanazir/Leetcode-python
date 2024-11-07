class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {'a','e','i','o','u','A','E','I','O','U'}
        st = list(s)
        i = 0
        j = len(st)-1

        while(i<=j):
            if st[i] not in vow:
                i+=1
            elif st[j] not in vow:
                j-=1
            else:
                temp = st[i]
                st[i] = st[j]
                st[j] = temp
                
                i+=1
                j-=1

            
        return "".join(st)


        
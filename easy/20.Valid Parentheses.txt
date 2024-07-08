class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {")": "(", "}": "{", "]": "["}

        for i in s:
            if stack and i in maps and stack[-1] == maps[i]:
                stack.pop()
            else:
                stack.append(i)
        
        return not stack
        #  s = "([{}])"  #s="[]"
        # stack=[]
        # top=-1
        # maps={")": "(", "}": "{", "]": "["}

        # for i in s:
        #     if top==-1:
        #         stack.append(i)
        #         top+=1
        #     else:
                
        #         if (i=="}") or(i== "]") or (i==")") :
        #             if stack[top]==maps[i]:
        #                 stack.pop()
        #                 top-=1
        #             else:
        #                 stack.append(i)
        #                 
        #         else:
        #             stack.append(i)
        #             top+=1
        # if stack:
        #     return True
        # else: 
        #     return False ///


            

                
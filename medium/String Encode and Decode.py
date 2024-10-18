class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "||"

    
        string="__".join(strs)
        return string



        

    def decode(self, s: str) -> List[str]:
        
        if s=="||":
            return []
        
        my_list = s.split('__')
        return my_list

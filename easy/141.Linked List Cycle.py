class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited= list()
        while(head is not None):
            if(head.next in visited):
                return True
            
            else:
            
                visited.append(head.next)
                head= head.next
        return False
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== []:
            return []
        
        
        start= head
        prev= None
        while (head is not None):
            start= head.next
            head.next= prev
            prev= head
            head= start
        return prev
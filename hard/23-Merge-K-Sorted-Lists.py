# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==[]:
            return None
        
        h1=lists[0]
        
        for i in range(len(lists)-1):
            h2=lists[i+1]
            if(h1.val<=h2.val):
                temp=h1
                h1=h1.next
                send=temp
            else:
                temp=h2
                h2=h2.next
                send=temp
            while(h1 and h2):
                if(h1.val<=h2.val):
                    temp.next=h1
                    temp=h1
                    h1=h1.next
                else:
                    temp.next=h2
                    temp=h2
                    h2=h2.next
            if h1 is None:
                temp.next=h2
            if h2 is None:
                temp.next=h1
            h1=send
        return send 




        
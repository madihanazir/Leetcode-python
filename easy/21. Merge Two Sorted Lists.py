
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if (list1 is None) and (list2 is None):
            return []


        h1= list1
        h2= list2
        n1=list1.next
        n2= list2.next
        if (h1.val <= h2.val):
            send=h1
        else:
            send=h2 

        while (h1 or h2):    
            if (h1.val <= h2.val):
                h1.next= h2
                temp= h2
            else:
                h2.next= h1
                temp= h1
            if(n1 and n2) and (n1.val<=n2.val):
                 temp.next= n1
            else:
                temp.next=n2
            h1,h2= n1,n2 

        return send




                
         
                 

        

        




            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
         #traversal for mid
        i= head;
        j= i.next;
        while(j and j.next):
            i= i.next
            j=j.next.next
        #reversal
        j=i.next
        i.next= None
        if (j):
            k=j.next
        else: 
            k=None

    
        while(j):
            j.next=i
            i=j
            j=k
            if(j):
                k=j.next


        #merge
        hn=head.next
        IN=i.next

        while(True):
            head.next= i
            i.next=hn
            head=hn
            i=IN
            if (not head or not i):
                break
            if (hn!= None):
                hn= hn.next
            else: 
                hn = None
            if (IN!=None):
                IN=IN.next
            else:
                IN= None
        
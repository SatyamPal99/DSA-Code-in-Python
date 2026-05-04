# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """temp=head
        d={}
        while temp!=None:
            d[temp]=d.get(temp,0)+1
            if d[temp]>1:
                return True
            temp=temp.next
        return False"""

        #Optimized approach (Using Tortoise and Hare Algo)....
        if head==None:
            return False
        up=head
        down=head
        while (up!=None and up.next!=None):
            down=down.next
            up=up.next.next
            if up==down:
                return True
        return False



        
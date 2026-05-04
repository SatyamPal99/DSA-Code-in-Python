# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        d={}
        while temp!=None:
            d[temp]=d.get(temp,0)+1
            if d[temp]>1:
                return temp
            temp=temp.next
        return None
        
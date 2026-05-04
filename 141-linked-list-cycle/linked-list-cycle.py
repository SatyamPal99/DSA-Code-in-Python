# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        d={}
        while temp!=None:
            d[temp]=d.get(temp,0)+1
            if d[temp]>1:
                return True
            temp=temp.next
        return False

        
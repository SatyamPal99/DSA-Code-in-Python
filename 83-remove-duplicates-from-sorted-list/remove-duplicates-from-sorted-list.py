# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        temp1=temp2=head
        prev=temp1
        temp2=temp2.next
        while temp2!=None:
            if temp1.val==temp2.val:
                prev=temp2
                temp2=temp2.next
            else:
                temp1.next=prev.next
                temp1=temp1.next
                prev=temp1
                temp2=temp2.next
        temp1.next=prev.next
        return head

        
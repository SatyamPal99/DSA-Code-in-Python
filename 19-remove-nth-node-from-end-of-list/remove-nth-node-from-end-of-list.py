# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        curr=head
        temp=0
        while curr:
            temp+=1
            curr=curr.next
        count=temp-n
        curr=head
        if count==0:
            return curr.next
        for i in range(1,count):
            curr=curr.next
        curr.next=curr.next.next
        return head
        
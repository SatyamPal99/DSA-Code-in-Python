# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        n=0
        temp=head
        while temp!=None:
            temp=temp.next
            n+=1
        count=k%(n)
        while(count):
            curr=head
            prev=head
            while prev.next.next!=None:
                prev=prev.next
            temp=prev.next
            prev.next=None
            temp.next=curr
            head=temp
            count-=1
        return head


        
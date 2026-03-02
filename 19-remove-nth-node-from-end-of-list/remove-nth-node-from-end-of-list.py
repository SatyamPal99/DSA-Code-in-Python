# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while temp!=None:
            c=c+1
            temp=temp.next
        curr=head
        prev=None
        k=c-n
        print(k)
        print(c)
        if k==0 :
            if k==0 and c==1:
                return None
            elif k==0 and c>1:
                head=head.next
                curr.next=None
                return head
            
        for i in range(0,k):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        curr.next=None
        return head
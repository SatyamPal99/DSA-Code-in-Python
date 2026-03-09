# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=head
        r=head
        c1=1
        while c1!=left:
            c1+=1
            l=l.next
        c2=1
        while c2!=right:
            c2+=1
            r=r.next
        

        while(c1<c2):
            b=l
            while b.next!=r:
                b=b.next
            temp=l.val
            l.val=r.val
            r.val=temp

            l=l.next
            c1+=1
            r=b
            c2-=1
        return head
        
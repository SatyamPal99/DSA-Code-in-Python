# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevNode=None
        while (temp!=None):
            kth=self.findKth(temp,k)
            if kth==None:
                if prevNode:
                    prevNode.next=temp
                break
            NextNode=kth.next
            kth.next=None
            self.reverse(temp)
            if temp==head:
                head=kth
            else:
                prevNode.next=kth
            prevNode=temp
            temp=NextNode
        return head
    
    def findKth(self,temp,k):
        k=k-1
        while(temp!=None and k>0):
            k=k-1
            temp=temp.next
        return temp
    def reverse(self,temp):
        prev=None
        curr=temp
        while temp!=None:
            temp=temp.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

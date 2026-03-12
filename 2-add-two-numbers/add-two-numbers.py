# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  ------If we have to create new linkedlist then always use dummyNode concept-------

        carry=0
        dummyNode=ListNode(-1)
        curr=dummyNode
        value=0
        while(l1!=None or l2!=None):
            sum=carry
            if(l1):
                sum=sum+l1.val
                l1=l1.next
            if(l2):
                sum=sum+l2.val
                l2=l2.next
            value=sum%10
            carry=sum//10
            new=ListNode(value)
            curr.next=new
            curr=curr.next
        if (carry):
            new=ListNode(carry)
            curr.next=new
            curr=curr.next
        return dummyNode.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """st=[]
        curr=head
        while curr:
            st.append(curr.val)
            curr=curr.next
        curr=head
        while curr:
            if curr.val==st.pop():
                curr=curr.next
            else:
                return False
        return True"""
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while (fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        end=self.reverse(slow.next)
        curr=head
        while end!=None:
            if curr.val==end.val:
                curr=curr.next
                end=end.next
            else:
                return False
        return True

    def reverse(self,head):
        pre=None
        curr=temp=head
        while curr:
            temp=temp.next
            curr.next=pre
            pre=curr
            curr=temp
        return pre

        
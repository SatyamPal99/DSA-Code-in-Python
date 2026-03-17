# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        # time = O(len(LL))+O(len-n)= O(len+len)
        """curr=head
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
        return head"""
        
        # optimized 
        slow=head
        fast=head
        while n>0:
            fast=fast.next
            n-=1
        if fast==None:
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
        
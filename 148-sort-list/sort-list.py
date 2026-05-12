# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """dummy=ListNode(-1)
        curr=dummy
        arr=[]
        temp=head
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        for i in range(len(arr)):
            new=ListNode(arr[i])
            curr.next=new
            curr=curr.next
        return dummy.next"""

        """temp=head
        arr=[]
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        temp=head
        i=0
        while temp!=None:
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head"""

        #optimized code (Using Inplace)
    
        if head==None or head.next==None:
            return head
        mid=self.findMid(head)
        left_head=head
        right_head=mid.next
        mid.next=None
        left_head=self.sortList(left_head)
        right_head=self.sortList(right_head)
        return self.merge(left_head,right_head)
    
    def findMid(self,head):
        low=head
        high=head
        while high.next!=None and high.next.next!=None:
            low=low.next
            high=high.next.next
        return low
    def merge(self,head1,head2):
        dummy=ListNode(-1)
        temp=dummy
        while head1!=None and head2!=None:
            if head1.val<head2.val:
                temp.next=head1
                head1=head1.next
                temp=temp.next
            elif head1.val>head2.val:
                temp.next=head2
                head2=head2.next
                temp=temp.next
            else:
                temp.next=head1
                temp=temp.next
                head1=head1.next
                temp.next=head2
                temp=temp.next
                head2=head2.next
        if head1==None:
            temp.next=head2
        elif head2==None:
            temp.next=head1

        return dummy.next


        
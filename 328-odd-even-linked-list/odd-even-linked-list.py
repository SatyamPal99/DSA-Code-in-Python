# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        """st1=[]
        st2=[]
        temp=head
        c=1
        while temp:
            if c%2==1:
                st1.append(temp.val)
            else:
                st2.append(temp.val)
            c+=1
            temp=temp.next
        temp=head
        c=0
        while temp:
            if st1:
                temp.val=st1.pop(0)
            else:
                temp.val=st2.pop(0)
            
            temp=temp.next
        return head"""

        """
        st=[]
        temp=head
        while temp!=None and temp.next!=None:
            st.append(temp.val)
            temp=temp.next.next
        if temp:
            st.append(temp.val)

        temp=head.next
        while temp!=None and temp.next!=None:
            st.append(temp.val)
            temp=temp.next.next
        if temp:
            st.append(temp.val)
        temp=head
        while temp!=None:
            temp.val=st.pop(0)
            temp=temp.next
        return head"""
# Optimized Approach.....
        odd=head
        even=head.next
        head1=head.next
        while (even!=None and even.next!=None):
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=head1
        return head
        


        
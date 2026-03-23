# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st=[]
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
        return True
        
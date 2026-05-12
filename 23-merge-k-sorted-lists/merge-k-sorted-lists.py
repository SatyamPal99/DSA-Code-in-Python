# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """arr=[]
        for i in range(len(lists)):
            temp=lists[i]
            while temp!=None:
                arr.append(temp.val)
                temp=temp.next
        arr.sort()
        dummy=ListNode(-1)
        temp=dummy
        for i in range(len(arr)):
            new=ListNode(arr[i])
            temp.next=new
            temp=temp.next
        return dummy.next"""

        # Optimized code
        if len(lists)==0:
            return None
        head=lists[0]
        for i in range(1,len(lists)):
            head=self.fun(head,lists[i])
        return head

    def fun(self,temp1, temp2):
        dummy=ListNode(-1)
        curr=dummy
        while temp1!=None and temp2!=None :
            if temp1.val<temp2.val:
                curr.next=temp1
                temp1=temp1.next
                curr=curr.next
            elif temp2.val<temp1.val:
                curr.next=temp2
                temp2=temp2.next
                curr=curr.next
            else:
                curr.next=temp1
                curr=curr.next
                temp1=temp1.next
                curr.next=temp2
                temp2=temp2.next
                curr=curr.next
        if temp1==None:
            curr.next=temp2
        elif temp2==None:
            curr.next=temp1
        return dummy.next   


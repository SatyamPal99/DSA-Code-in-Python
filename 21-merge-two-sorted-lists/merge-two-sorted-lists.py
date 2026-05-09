# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """arr=[]
        temp1=list1
        temp2=list2
        while temp1!=None:
            arr.append(temp1.val)
            temp1=temp1.next
        while temp2!=None:
            arr.append(temp2.val)
            temp2=temp2.next
        arr.sort()
        head=None
        for i in range(len(arr)):
            if i==0:
                head=ListNode(arr[i])
                temp=head
            else:
                new=ListNode(arr[i])
                temp.next=new
                temp=temp.next
        return head"""

        #Optimized 
        temp1=list1
        temp2=list2
        head=ListNode(-1)
        temp=head
        while(temp1!=None and temp2!=None ):
            if temp1.val<temp2.val:
                temp.next=temp1
                temp1=temp1.next
                temp=temp.next
            elif temp1.val>temp2.val:
                temp.next=temp2
                temp2=temp2.next
                temp=temp.next
            else:
                temp.next=temp1
                temp1=temp1.next
                temp=temp.next
                temp.next=temp2
                temp2=temp2.next
                temp=temp.next
        if temp2==None:
            temp.next=temp1
        elif temp1==None:
            temp.next=temp2
        return head.next

                

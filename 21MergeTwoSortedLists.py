# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=ListNode(0)
        l=a
        if not l1 and not l2:
            return a.next
        if l1 and l2:
            while l1 and l2:
                if l1.val>=l2.val:
                    l.next=ListNode(l2.val)
                    l=l.next
                    l2=l2.next
                else:
                    l.next=ListNode(l1.val)
                    l=l.next
                    l1=l1.next
        if l1:
            while l1:
                l.next=ListNode(l1.val)
                l=l.next
                l1=l1.next
        if l2:
            while l2:
                l.next=ListNode(l2.val)
                l=l.next
                l2=l2.next
        return a.next
if __name__=='__main__':
    arr1=[1,2,4]
    arr2=[1,3,4]
    p=ListNode(arr1[0])
    l1=p
    for i in arr1[1:]:
        l1.next=ListNode(i)
        l1=l1.next
    l1=p
    p=ListNode(arr2[0])
    l2=p
    for i in arr2[1:]:
        l2.next=ListNode(i)
        l2=l2.next
    l2=p
    solution=Solution()
    result=solution.mergeTwoLists(l1,l2)
    if result:
        while result:
            print(result.val)
            result=result.next

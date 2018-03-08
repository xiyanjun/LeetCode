# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        a=head
        while a.next:
            if a.val==a.next.val:
                a.next=a.next.next
            else:
                a=a.next
        return head
if __name__=='__main__':
    nums=[]
    if len(nums)==0:
        head=None
    else:
        head=ListNode(nums[0])
        m=head
        for i in nums:
            m.next=ListNode(i)
            m=m.next
    solution=Solution()
    result=solution.deleteDuplicates(head)
    outres=[]
    while result:
        outres.append(result.val)
        result=result.next
    print(outres)





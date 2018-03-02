
class ListNode: # Definition for singly-linked list.
    def __init__(self, x):
          self.val = x
          self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        n=ListNode(0)
        m=n
        flag=0
        while l1 and l2:
            m.next = ListNode((l1.val + l2.val + flag) % 10)
            flag = (l1.val+l2.val+flag)//10
            l2=l2.next
            l1 = l1.next
            m=m.next
        if l1 :
            while l1:
                m.next =ListNode((l1.val + flag) % 10)
                flag = (l1.val + flag) // 10
                l1 = l1.next
                m = m.next
        if l2 :
            while l2:
                m.next = ListNode((l2.val +flag)%10)
                flag=(l2.val+flag)//10
                l2=l2.next
                m=m.next
        if flag==1:
            m.next=ListNode(1)
        return n.next
if __name__=='__main__':
    a=ListNode(0)
    b=a
    for i in [2,4,3]:
        b.next=ListNode(i)
        b=b.next
    l1=a.next
    a=ListNode(0)
    b=a
    for i in [5,6,4]:
        b.next=ListNode(i)
        b=b.next
    l2=a.next
    solution=Solution()
    n=solution.addTwoNumbers(l1,l2)
    outnum=[]
    while n:
        outnum.append(n.val)
        n=n.next
    print(outnum)
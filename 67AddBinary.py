class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a[::-1]
        b=b[::-1]
        c=''
        flag=0
        if a and b:
            while a and b:
                c+=str((int(a[0])+int(b[0])+flag)%2)
                flag=(int(a[0])+int(b[0])+flag)//2
                a=a[1:]
                b=b[1:]
        if a:
            while a:
                c+=str((int(a[0])+flag)%2)
                flag=(int(a[0])+flag)//2
                a=a[1:]
        if b:
            while b:
                c+=str((int(b[0])+flag)%2)
                flag=(int(b[0])+flag)//2
                b=b[1:]
        if flag==1:
            c+='1'
        c=c[::-1]
        return c
if __name__=='__main__':
    a='11'
    b='1'
    solution=Solution()
    result=solution.addBinary(a,b)
    print(result)
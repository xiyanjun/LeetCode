class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=2**31 or x<(-(2**31)) or x==0:
            return 0
        else:
            if x>0:
                flag=1
            else:
                flag=-1
            x=abs(x)
            new_x=0
            while x:
                new_x=new_x*10+x%10
                x=x//10
            new_x=flag*new_x
            if new_x >= 2 ** 31 or new_x < (-(2 ** 31)) or new_x == 0:
                return 0
        return new_x
if __name__=='__main__':
    solution=Solution()
    new_x=solution.reverse(123)
    print(new_x)

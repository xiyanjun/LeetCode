class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=x
        while a**2-x>=1:
            a=a/2+x/(2*a)
        return int(a)
if __name__=='__main__':
    x=4
    solution=Solution()
    result=solution.mySqrt(x)
    print(result)

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or x>=2**31:
            return False
        else:
            renum=0
            b=x
            while x:
                renum=renum*10+x%10
                if renum >= 2 ** 31:
                    return False
                x=x//10
            if renum==b:
                return True
            else:
                return False
if __name__=='__main__':
    solution=Solution()
    outbool=solution.isPalindrome(-2147483648)
    print(outbool)

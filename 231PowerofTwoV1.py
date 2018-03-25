class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0:
            if n==1:
                return True
            elif n%2==0:
                n=n/2
            else:
                return False
        return False
def main():
    n=1
    solution=Solution()
    result=solution.isPowerOfTwo(n)
    print(result)
if __name__=='__main__':
    main()
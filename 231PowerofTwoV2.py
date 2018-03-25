class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and bin(n).count('1')==1
def main():
    n=1
    solution=Solution()
    result=solution.isPowerOfTwo(n)
    print(result)
if __name__=='__main__':
    main()
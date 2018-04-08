class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>0:
            n//=5
            count+=n
        return count
def main():
    n=0
    solution=Solution()
    result=solution.trailingZeroes(n)
    print(result)
if __name__=='__main__':
    main()

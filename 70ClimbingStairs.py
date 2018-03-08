class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        F=list(range(n+1))
        F[0]=1
        F[1]=1
        for i in range(2,n+1):
            F[i]=F[i-1]+F[i-2]
        return F[n]
if __name__=='__main__':
    solution=Solution()
    result=solution.climbStairs(2)
    print(result)
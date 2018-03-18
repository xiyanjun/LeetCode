class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum=0
        for i in nums:
            sum+=i
        if sum%2==1:
            return False
        target=sum//2
        dp={}
        dp[0]=True
        for j in nums:
            if j==target:
                return True
            if j<target:
                for k in range(target,j,-1):
                    dp[k]=dp.get(k) or dp.get(k-j)
            dp[j]=True
            if dp.get(target)==True:
                return True
        return False
def main():
    nums=[1,5,11,5]
    solution=Solution()
    result=solution.canPartition(nums)
    print(result)
if __name__=='__main__':
    main()
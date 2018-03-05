class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxendhere=maxsofar=nums[0]
        for i in nums[1:]:
            maxendhere=max(i,maxendhere+i)
            maxsofar=max(maxsofar,maxendhere)
        return maxsofar
if __name__=='__main__':
    solution=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    result=solution.maxSubArray(nums)
    print(result)

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]<target<nums[i]:
                return i
if __name__=='__main__':
    nums=[1,3,5,6]
    target=5
    solution=Solution()
    result=solution.searchInsert(nums,target)
    print(result)

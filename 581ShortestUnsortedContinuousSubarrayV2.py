class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
#left
        while left<len(nums)-1 and nums[left]<=nums[left+1]:
            left+=1
        if left==len(nums)-1:
            return 0
        min_right=min(nums[left+1:])
        while left>=0 and nums[left]>min_right:
            left-=1
#right
        while right>0 and nums[right]>=nums[right-1]:
            right-=1
        if right==0:
            return 0
        max_left=max(nums[:right])
        while right<=len(nums)-1 and max_left>nums[right]:
            right+=1
        return right-left-1
def main():
    nums=[2,6,4,8,10,9,15]
    solution=Solution()
    result=solution.findUnsortedSubarray(nums)
    print(result)
if __name__=='__main__':
    main()
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif mid%2==1:
                if nums[mid]==nums[mid-1]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[mid]==nums[mid+1]:
                    left=mid+2
                else:
                    right=mid
        if left==right:
            return nums[left]

def main():
    nums=[1,1,2]
    solution=Solution()
    result=solution.singleNonDuplicate(nums)
    print(result)
if __name__=='__main__':
    main()


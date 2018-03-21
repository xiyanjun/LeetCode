class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        size=len(nums)+1
        for i in range(size):
            a=a^i
        for i in range(len(nums)):
            a=a^nums[i]
        return a
def main():
    nums=[3,0,1]
    solution=Solution()
    result=solution.missingNumber(nums)
    print(result)
if __name__=='__main__':
    main()
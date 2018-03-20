class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
           a^=nums[i]
        return a
def main():
    nums=[2,2,1]
    solution=Solution()
    result=solution.singleNumber(nums)
    print(result)
if __name__=='__main__':
    main()
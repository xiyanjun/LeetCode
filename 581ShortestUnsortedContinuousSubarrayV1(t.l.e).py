class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        lenth=len(nums)
        while nums:
            if nums[0]==min(nums):
                nums=nums[1:]
                count+=1
            else:
                break
        while nums:
            if nums[-1]==max(nums):
                nums=nums[:-1]
                count+=1
            else:
                break
        return lenth-count
def main():
    nums=[2,6,4,8,10,9,15]
    solution=Solution()
    result=solution.findUnsortedSubarray(nums)
    print(result)
if __name__=='__main__':
    main()
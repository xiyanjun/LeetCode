class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]*=-1
        return res
def main():
    nums=[4,3,2,7,8,2,3,1]
    solution=Solution()
    result=solution.findDuplicates(nums)
    print(result)
if __name__=='__main__':
    main()
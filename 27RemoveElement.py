class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size=len(nums)
        j=0
        for i in range(size):
           if nums[i]==val:
               i+=1
           else:
               nums[j]=nums[i]
               i+=1
               j+=1
        return j
if __name__=='__main__':
    solution=Solution()
    nums=[3,2,2,3]
    val=3
    result=solution.removeElement(nums,val)
    print(result)
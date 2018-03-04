class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        j=1
        size=len(nums)
        while j<size:
            if nums[i-1]==nums[j]:
                j+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
        return min(i,size)
if __name__=='__main__':
    solution=Solution()
    nums=[1,1,2]
    result=solution.removeDuplicates(nums)
    print(result)


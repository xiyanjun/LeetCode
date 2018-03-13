class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#从10000到1的测试数组导致超时，所以需要修改判断。
        size=len(nums)
        nums.extend(nums)
        for i in range(size):
            j=1
            while j<size:
                if nums[i]<nums[i+j]:
                    nums[i]=nums[i+j]
                    break
                else:
                    j+=1
            if j==size:
                nums[i]=-1
        nums=nums[:size]
        return nums
def main():
    nums=[1,2,1]
    solution=Solution()
    result=solution.nextGreaterElements(nums)
    print(result)
if __name__=='__main__':
    main()


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[-1]*len(nums)
        for i in range(len(nums)*2):
            i=i%(len(nums))
            while stack and nums[stack[-1]]<nums[i]:
                res[stack.pop()]=nums[i]
            stack.append(i)
        return res
def main():
    nums=[1,2,1]
    solution=Solution()
    result=solution.nextGreaterElements(nums)
    print(result)
if __name__=='__main__':
    main()

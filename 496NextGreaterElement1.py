class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        for j in range(len(findNums)):
            a=dict.get(findNums[j])
            b=a+1
            findNums[j]=-1
            while b<len(nums):
                if nums[a]<nums[b]:
                    findNums[j]=nums[b]
                    break
                else:
                    b=b+1
        return findNums
def main():
    findNums=[4,1,2]
    nums=[1,3,4,2]
    solution=Solution()
    result=solution.nextGreaterElement(findNums,nums)
    print(result)
if __name__=='__main__':
    main()

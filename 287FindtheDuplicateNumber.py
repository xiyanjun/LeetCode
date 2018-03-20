class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        min=0
        max=size-1
        while(min<max):
            mid = min + (max - min) // 2
            count=0
            for i in nums:
                if i<=mid:
                    count+=1
            if count>mid:
                max=mid
            else:
                min=mid+1
        return max
def main():
    nums=[1,1]
    solution=Solution()
    result=solution.findDuplicate(nums)
    print(result)
if __name__=='__main__':
    main()
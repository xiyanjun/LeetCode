class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        k=k%size
        self.reversePart(nums,0,size-k-1)
        self.reversePart(nums,size-k,size-1)
        self.reversePart(nums,0,size-1)
        return nums
    def reversePart(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
def main():
    nums=[1]
    k=0
    solution=Solution()
    result=solution.rotate(nums,k)
    print(result)
if __name__=='__main__':
    main()
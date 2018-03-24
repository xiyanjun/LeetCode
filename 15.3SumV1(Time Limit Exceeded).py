class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.append([nums[i],nums[j],nums[k]])
        for i in res:
            i.sort()
        res.sort(key=lambda x:x[1])
        res.sort(key=lambda x:x[0])
        i=1
        while i<len(res):
            if res[i][0]==res[i-1][0] and res[i][1]==res[i-1][1]:
                del res[i]
            else:
                i+=1
        return res
def main():
    nums=[-1,0,1,2,-1,-4]
    solution=Solution()
    result=solution.threeSum(nums)
    print(result)
if __name__=='__main__':
    main()


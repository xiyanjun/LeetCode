class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        m=len(nums)-2
        for i in range(m):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,h=i+1,m+1
            while l<h:
                s=nums[i]+nums[l]+nums[h]
                if s==0:
                    res.append([nums[i],nums[l],nums[h]])
                    while l<h and nums[h]==nums[h-1]:
                        h=h-1
                    while l<h and nums[l]==nums[l+1]:
                        l=l+1
                    h=h-1
                    l=l+1
                elif s<0:
                    l=l+1
                else :
                    h=h-1
        return res
def main():
    nums=[-1,0,1,2,-1,-4]
    solution=Solution()
    result=solution.threeSum(nums)
    print(result)
if __name__=='__main__':
    main()


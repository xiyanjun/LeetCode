class Solution:
    def twoSum(self,nums,target):
        dict={}
        for i in range(len(nums)):
            if(dict.get(target-nums[i],None)==None):
                dict[nums[i]]=i
            else:
                return(dict[target-nums[i]],i)
if __name__=='__main__':
    nums=[3,2,4]
    target=6
    solution=Solution()
    n=solution.twoSum(nums,target)
    print(n)
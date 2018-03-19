class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        def search(s,count,sums,nums):
            if count==k and sums!=n:
                return
            if count==k and sums==n:
                ans.append(nums)
                return
            for i in range(s+1,10):
                search(i,count+1,sums+i,nums+[i])
        search(0,0,0,[])
        return ans
def main():
    k=3
    n=9
    solution=Solution()
    result=solution.combinationSum3(k,n)
    print(result)
if __name__=='__main__':
    main()
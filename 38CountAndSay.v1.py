class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        for _ in range(2,n+1):
            count=1
            i=0
            reset=''
            while i<(len(s)):
                if i+count<len(s) and s[i]==s[i+count]:
                    count+=1
                else:
                    reset+=str(count)+s[i]
                    i=i+count
                    count=1
            s=reset
        return s
if __name__=='__main__':
    n=1
    solution=Solution()
    result=solution.countAndSay(n)
    print(result)

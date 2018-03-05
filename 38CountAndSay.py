class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        if n>1:
            size=len(solution.countAndSay(n-1))
            i=0
            outstr=''
            while i<size:
                count=1
                for j in range(i,size):
                    if i+count<size and solution.countAndSay(n-1)[i]==solution.countAndSay(n-1)[i+count]:
                        count=count+1
                    else:
                        outstr+=str(count)
                        outstr+=str(solution.countAndSay(n-1)[i])
                        break
                i=i+count
        return outstr
if __name__=='__main__':
    n=1
    solution=Solution()
    result=solution.countAndSay(n)
    print(result)

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num)==k:
            num='0'
            return num
        for _ in range(k):
            gene=num[0]
            for i in range(1,len(num)):
                if i==len(num)-1:
                    if num[i]>=num[i-1]:
                        num=gene
                    else:
                        num=gene[:-1]+num[i:]
                elif num[i]>=num[i-1]:
                    gene+=num[i]
                else :
                    num=gene[:-1]+num[i:]
                    break
        for i in range(len(num)):
            if len(num)>1 and num[0]=='0':
                num=num[1:]
            else:
                return num
def main():
    num='1432219'
    k=3
    solution=Solution()
    result=solution.removeKdigits(num,k)
    print(result)
if __name__=='__main__':
    main()
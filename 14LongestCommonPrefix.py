class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        else:
            for i in range(len(strs)):
                lenth0=len(strs[0])
                lenth1=len(strs[i])
                if lenth0<lenth1:
                    lenth=lenth0
                else:
                    lenth=lenth1
                strs[0]=strs[0][0:lenth]
                for j in range(lenth):
                    if strs[0][j]!=strs[i][j]:
                        strs[0]=strs[0][0:j]
                        break
            return strs[0]
if __name__=='__main__':
    solution=Solution()
    prefix=solution.longestCommonPrefix([])
    print(prefix)
